n, m, a, b, r= map(int, input().split())

full_tickets = n // m

remaining_rides = n % m

cost_using_m_tickets = full_tickets * b + min(remaining_rides * a, b)

cost_using_single_tickets = n * a

min_cost = min(cost_using_m_tickets, cost_using_single_tickets)

print(min_cost)
