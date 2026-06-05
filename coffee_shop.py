"""
Coffee Shop Simulation using SimPy
Measures impact of staffing and equipment on customer experience
"""

import simpy
import random
import statistics

# ========== SIMULATION SETTINGS ==========
NUM_BARISTAS = 2           # Number of coffee makers
NUM_REGISTERS = 1          # Number of cashiers
CUSTOMER_INTERVAL = 1.5    # Minutes between arrivals
ORDER_TIME = 1.5           # Minutes to take order
BREW_TIME = 2.5            # Minutes to make coffee
SIMULATION_HOURS = 8       # Hours to run
RANDOM_SEED = 42

# ========== DATA COLLECTION ==========
wait_times = []
orders_completed = 0

def coffee_shop(env, register, barista):
    """Process for each customer"""
    global orders_completed
    
    arrival_time = env.now
    
    # Step 1: Wait for register
    with register.request() as order_req:
        yield order_req
        yield env.timeout(random.expovariate(1.0/ORDER_TIME))
    
    # Step 2: Wait for barista
    with barista.request() as brew_req:
        yield brew_req
        yield env.timeout(random.expovariate(1.0/BREW_TIME))
    
    total_wait = env.now - arrival_time
    wait_times.append(total_wait)
    orders_completed += 1

def customer_arrivals(env, register, barista):
    """Generate customers"""
    while True:
        yield env.timeout(random.expovariate(1.0/CUSTOMER_INTERVAL))
        env.process(coffee_shop(env, register, barista))

def run_simulation(num_registers, num_baristas, sim_mins):
    """Run one simulation with given parameters"""
    global wait_times, orders_completed
    
    # Reset data for this run
    wait_times = []
    orders_completed = 0
    
    # Create environment
    env = simpy.Environment()
    register = simpy.Resource(env, capacity=num_registers)
    barista = simpy.Resource(env, capacity=num_baristas)
    
    # Start customer generation
    env.process(customer_arrivals(env, register, barista))
    
    # Run simulation
    env.run(until=sim_mins)
    
    # Calculate average wait time (handle empty list case)
    avg_wait = statistics.mean(wait_times) if wait_times else 0
    
    return {
        'avg_wait': avg_wait,
        'orders_completed': orders_completed,
        'customers_per_hour': orders_completed / (sim_mins / 60)
    }

def print_results(scenario_name, results):
    """Print results in a nice formatted way"""
    print(f"\n{'='*50}")
    print(f"{scenario_name}")
    print(f"{'='*50}")
    print(f"Orders completed:     {results['orders_completed']}")
    print(f"Customers per hour:   {results['customers_per_hour']:.1f}")
    print(f"Average wait time:    {results['avg_wait']:.2f} minutes")

# ========== RUN SIMULATION ==========
if __name__ == "__main__":
    # Set random seed for reproducible results
    random.seed(RANDOM_SEED)
    sim_minutes = SIMULATION_HOURS * 60
    
    print("\n☕ COFFEE SHOP SIMULATION")
    print(f"Running for {SIMULATION_HOURS} hours\n")
    
    # Experiment 1: Baseline (1 cashier, 1 barista)
    results1 = run_simulation(1, 1, sim_minutes)
    print_results("BASELINE: 1 cashier, 1 barista", results1)
    
    # Experiment 2: Extra barista only (1 cashier, 2 baristas)
    results2 = run_simulation(1, 2, sim_minutes)
    print_results("EXTRA BARISTA: 1 cashier, 2 baristas", results2)
    
    # Experiment 3: Extra cashier only (2 cashiers, 1 barista)
    results3 = run_simulation(2, 1, sim_minutes)
    print_results("EXTRA REGISTER: 2 cashiers, 1 barista", results3)
    
    # Experiment 4: Fully staffed (2 cashiers, 2 baristas)
    results4 = run_simulation(2, 2, sim_minutes)
    print_results("FULL STAFF: 2 cashiers, 2 baristas", results4)
    
    # Impact Analysis
    print(f"\n{'='*50}")
    print(" IMPACT ANALYSIS (compared to baseline)")
    print(f"{'='*50}")
    
    improvement_barista = ((results1['avg_wait'] - results2['avg_wait']) / results1['avg_wait']) * 100
    improvement_cashier = ((results1['avg_wait'] - results3['avg_wait']) / results1['avg_wait']) * 100
    improvement_both = ((results1['avg_wait'] - results4['avg_wait']) / results1['avg_wait']) * 100
    
    print(f"Adding 1 barista:     {improvement_barista:.1f}% reduction in wait time")
    print(f"Adding 1 cashier:     {improvement_cashier:.1f}% reduction in wait time")
    print(f"Adding both:          {improvement_both:.1f}% reduction in wait time")
    
    print("\n Simulation complete!")