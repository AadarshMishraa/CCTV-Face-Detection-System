# Contributing to Facial Recognition System

First off, thank you for considering contributing to this project! It's people like you that make this tool better for everyone.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if possible**
- **Include your environment details** (OS, Python version, browser, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List any similar features in other applications**

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code follows the existing style
6. Issue that pull request!

## Development Process

### Setting Up Your Development Environment

```bash
# Clone your fork
git clone https://github.com/your-username/facial-recognition-system.git
cd facial-recognition-system

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
cd backend
pip install -r requirements.txt
```

### Coding Standards

#### Python
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused
- Write comments for complex logic

#### JavaScript
- Use ES6+ features
- Use `const` and `let` instead of `var`
- Use meaningful variable names
- Add comments for complex logic
- Keep functions small and focused

#### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Example:
```
Add video batch processing feature

- Implement queue system for multiple videos
- Add progress tracking
- Update UI to show batch status

Fixes #123
```

### Testing

Before submitting a pull request:

1. Test your changes locally
2. Ensure all existing tests pass
3. Add new tests for new features
4. Test on different browsers (if frontend changes)
5. Test with different image/video formats

### Documentation

- Update README.md if you change functionality
- Update DEPLOYMENT.md if you change deployment process
- Add inline comments for complex code
- Update API documentation if you change endpoints

## Project Structure

```
facial-recognition-system/
├── backend/           # Flask API
│   ├── app.py        # Main application
│   └── face_detector.py  # Detection logic
├── frontend/         # Web interface
│   ├── index.html
│   ├── style.css
│   └── script.js
└── docs/            # Documentation
```

## Areas for Contribution

### High Priority
- [ ] Add unit tests
- [ ] Improve error handling
- [ ] Add progress indicators for long operations
- [ ] Optimize video processing speed
- [ ] Add support for more video formats

### Medium Priority
- [ ] Add database integration
- [ ] Implement user authentication
- [ ] Add batch processing
- [ ] Create API documentation
- [ ] Add Docker support

### Low Priority
- [ ] Mobile app
- [ ] Real-time stream processing
- [ ] Advanced filtering options
- [ ] Export reports feature
- [ ] Email notifications

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
