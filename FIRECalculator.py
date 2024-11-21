class FIRECalculator:
    def __init__(self):
        self.starting_savings = 0
        self.post_tax_annual_income = 0 # Including
        self.annual_expenses = 0
        self.investment_growth_rate = 0.07  # Default to 7%
        self.inflation_rate = 0.03         # Default to 2%
        self.retirement_goal = 0
        self.yearly_adjustments = {}       # Custom values for specific years

    def set_base_inputs(self, starting_savings, post_tax_annual_income, annual_expenses, retirement_goal):
        self.starting_savings = starting_savings
        self.post_tax_annual_income = post_tax_annual_income
        self.annual_expenses = annual_expenses
        self.retirement_goal = retirement_goal

    def add_yearly_adjustment(self, year, income=None, expenses=None):
        self.yearly_adjustments[year] = {'income': income, 'expenses': expenses}

    def calculate_progress(self, years=30):
        savings = self.starting_savings
        yearly_data = []

        for year in range(1, years + 1):
            income = self.post_tax_annual_income
            expenses = self.annual_expenses

            # Apply custom adjustments
            if year in self.yearly_adjustments:
                if self.yearly_adjustments[year]['income'] is not None:
                    income = self.yearly_adjustments[year]['income']
                if self.yearly_adjustments[year]['expenses'] is not None:
                    expenses = self.yearly_adjustments[year]['expenses']

            # Calculate yearly savings and growth
            savings += income - expenses
            savings *= (1 + self.investment_growth_rate)  # Apply growth
            expenses *= (1 + self.inflation_rate)         # Adjust for inflation

            yearly_data.append({
                'year': year,
                'income': income,
                'expenses': expenses,
                'savings': savings,
                'goal_met': savings >= self.retirement_goal
            })

            # Stop if the goal is met
            if savings >= self.retirement_goal:
                break

        return yearly_data

    def display_results(self, yearly_data):
        print(f"{'Year':<10}{'Income':<15}{'Expenses':<15}{'Savings':<15}{'Goal Met':<10}")
        for data in yearly_data:
            print(f"{data['year']:<10}{data['income']:<15.2f}{data['expenses']:<15.2f}{data['savings']:<15.2f}{data['goal_met']}")

# Example Usage
calculator = FIRECalculator()
calculator.set_base_inputs(starting_savings=200000, post_tax_annual_income=50000, annual_expenses=30000, retirement_goal=1000000)
calculator.add_yearly_adjustment(year=5, income=60000)  # Custom income in year 5
calculator.add_yearly_adjustment(year=10, expenses=35000)  # Custom expenses in year 10
result = calculator.calculate_progress(years=40)
calculator.display_results(result)
