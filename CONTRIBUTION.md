# Contributing to Burpy CLI Framework

First off, thank you for considering contributing to Burpy! It's people like you that make Burpy such a great tool.

## Code of Conduct

This project and everyone participating in it are governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

1. **Ensure the bug is not already reported** by searching existing GitHub issues.

2. If you can't find an existing issue, open a new one with:
   - A clear title and description
   - Specific steps to reproduce the problem
   - Expected behavior
   - Actual behavior
   - Python version
   - Burpy version


### Suggesting Enhancements

1. Open an issue with:
   - A clear title and description
   - Motivation for the enhancement
   - Detailed proposal
   - Potential benefits

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


#### Pull Request Guidelines

- Write clear, concise commit messages
- Include tests for new features
- Update documentation
- Ensure all tests pass
- Follow the project's coding style


### Development Setup
1. Clone the repository

```bash
git clone https://github.com/yourusername/burpy.git
cd burpy
```

2. Create a virtual enviorntment 

```bash
poetry shell
```

3. For now Burpy is dependent on **0** third party dependency but you can download any dependency if required

```bash
poetry install --dev
```

4. Run tests 

```bash
pytest
```

## Coding Style

- Follow PEP 8 guidelines
- Use type hints
- Write docstrings for all public methods
- Keep functions and methods focused and concise

## Documentation

- Update docstrings when adding/changing functionality
- Keep README.md and other documentation up to date
- Use type hints and descriptive variable names

## Feature Development Workflow

1. Discuss the feature in an issue
2. Get approval from maintainers
3. Create a detailed implementation plan
4. Write tests first (Test-Driven Development)
5. Implement the feature
6. Ensure 100% test coverage
7. Update documentation
8. Submit a pull request

## Types of Contributions We Need

- Bug fixes
- Documentation improvements
- Performance optimizations
- New feature implementations
- Improved error handling
- Additional CLI command support

## Questions?

If you have any questions, feel free to:

- Open an issue with the `question` label
- Join our discussion forums
- Reach out to maintainers directly

## Maintainers

- Mukund - Primary Maintainers
- [You](https://github.com/z44d/tgram/graphs/contributors) - Maybe Next ?

## Financial Contributions

If you want to support the project financially, consider:

- Sponsoring on GitHub Sponsors
- Contributing through Open Collective
- Sending a one-time donation

## License

By contributing, you agree that your contributions will be licensed under the project's MIT License.

> Thank you for your interest in improving Burpy! 🚀