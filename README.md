### Automated UI Testing for Demoblaze

This project is designed to demonstrate functional UI testing using Selenium WebDriver, Python, and Pytest. It follows the Page Object Model (POM) and includes test cases for user authentication, adding items to the cart, and the checkout process.

## Project Structure
Pages/
  base_page.py        # Base class with common methods
  cart_page.py        # Page object for the shopping cart

tests/
  test_1_auth.py      # Tests for user authentication
  test_2_cart.py      # Tests for adding items to the cart
  test_3_checkout.py  # Tests for the checkout process

utils/
  browser.py          # WebDriver setup and configuration
  config.py           # Configuration settings (e.g., URLs)

.gitlab-ci.yml        # CI/CD pipeline configuration. Not ready yet.
requirements.txt      # List of dependencies
README.md            # Project documentation

## Installation

Clone the repository:
```
git clone https://github.com/nbezverkhaya/Ecommerce_test_project.git
```
Navigate to the project directory

Install the dependencies:
```
pip install -r requirements.txt
```

## Dependencies

The main dependencies are listed in requirements.txt, including:

* selenium
* pytest
* webdriver-manager

## Contributing

Feel free to fork the repository and submit pull requests. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details