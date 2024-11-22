class FIRECalculator:
    def __init__(self):
        self.starting_savings = 0
        self.post_tax_annual_income = 0
        self.annual_expenses = 0
        self.investment_growth_rate = 0.07  # Default to 7%
        self.inflation_rate = 0.03         # Default to 3%
        self.retirement_goal = 0
        self.age = 0                       # User's current age
        self.yearly_adjustments = {}       # Custom values for specific years

    def set_base_inputs(
        self,
        starting_savings,
        post_tax_annual_income,
        annual_expenses,
        age,
        retirement_goal=None,
        investment_growth_rate=0.07,
        inflation_rate=0.03
    ):
        self.starting_savings = starting_savings
        self.post_tax_annual_income = post_tax_annual_income
        self.annual_expenses = annual_expenses
        self.age = age
        self.investment_growth_rate = investment_growth_rate
        self.inflation_rate = inflation_rate
        # Default retirement goal to 25x annual expenses if not provided
        self.retirement_goal = retirement_goal if retirement_goal is not None else 25 * annual_expenses

    def add_yearly_adjustment(self, year, income=None, expenses=None):
        """Add custom adjustments for specific years."""
        self.yearly_adjustments[year] = {'income': income, 'expenses': expenses}

    def calculate_progress(self, years=30):
        """Calculate yearly net worth growth with inflation-adjusted returns."""
        savings = self.starting_savings
        yearly_data = []
        real_growth_rate = self.investment_growth_rate - self.inflation_rate
        current_age = self.age

        for year in range(1, years + 1):
            income = self.post_tax_annual_income
            expenses = self.annual_expenses

            # Apply custom adjustments for income and expenses
            if year in self.yearly_adjustments:
                if self.yearly_adjustments[year]['income'] is not None:
                    income = self.yearly_adjustments[year]['income']
                if self.yearly_adjustments[year]['expenses'] is not None:
                    expenses = self.yearly_adjustments[year]['expenses']

            # Adjust savings with compounding growth and annual contributions
            savings = savings * (1 + real_growth_rate) + (income - expenses)

            # Log yearly data
            yearly_data.append({
                'year': year,
                'age': current_age + year,
                'income': income,
                'expenses': expenses,
                'savings': savings,
                'goal_met': savings >= self.retirement_goal
            })

            # Stop early if retirement goal is met
            if savings >= self.retirement_goal:
                break

        return yearly_data

    def display_results(self, yearly_data):
        """Display results in a readable table format."""
        print(f"{'Year':<10}{'Age':<10}{'Income':<15}{'Expenses':<15}{'Savings':<15}{'Goal Met':<10}")
        for data in yearly_data:
            print(f"{data['year']:<10}{data['age']:<10}{data['income']:<15.2f}{data['expenses']:<15.2f}{data['savings']:<15.2f}{data['goal_met']}")

# Example Usage
calculator = FIRECalculator()
calculator.set_base_inputs(
    starting_savings=200000,
    post_tax_annual_income=60000,
    annual_expenses=30000,
    age=30,
    retirement_goal=None,  # Defaults to 25 * annual_expenses
    investment_growth_rate=0.07,
    inflation_rate=0.03
)
# calculator.add_yearly_adjustment(year=5, income=70000)  # Custom income in year 5
# calculator.add_yearly_adjustment(year=10, expenses=35000)  # Custom expenses in year 10
result = calculator.calculate_progress(years=40)
calculator.display_results(result)
