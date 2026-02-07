# Contributing to EquinoxDB

Thank you for your interest in contributing to EquinoxDB! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS

### Suggesting Features

Feature requests are welcome! Please open an issue describing:
- The problem you're trying to solve
- Your proposed solution
- Any alternatives you've considered

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Run tests** (when available)
   ```bash
   pytest
   ```
5. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

## Development Setup

```bash
# Clone the repository
git clone https://github.com/BernardoParrales/EquinoxDB.git
cd EquinoxDB

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Install development dependencies (when available)
pip install -r requirements-dev.txt
```

## Code Style

- Follow [PEP 8](https://pep8.org/)
- Use meaningful variable names
- Add docstrings to public functions and classes
- Keep functions focused and small

## Testing

- Write tests for new features
- Ensure existing tests pass
- Aim for good test coverage

## Questions?

Feel free to open an issue for any questions or clarifications.

Thank you for contributing! 🙏
