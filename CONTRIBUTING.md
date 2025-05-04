# Contributing Guidelines for the Discord Ticketing Bot


[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

Thank you for your interest in contributing to the Discord Ticketing Bot! We appreciate your help in making this bot even better for the community.

This document provides guidelines on how you can contribute to the project. Please read these instructions carefully before getting started.

## How You Can Contribute

There are several ways you can contribute:

* **Report Bugs:** Help us identify and resolve issues by reporting bugs clearly and thoroughly.
* **Request Features:** Suggest new features that could enhance the user experience.
* **Contribute Code:** Implement new features, fix bugs, or refactor existing code.
* **Improve Documentation:** Help make the documentation clearer and more comprehensive.
* **Provide Support:** Assist other users by answering their questions and helping them troubleshoot problems.

## Reporting Bugs (Issues)

If you encounter a bug, please follow these steps to report it:

1.  **Check for Existing Bugs:** Search the [open issues](https://github.com/K0lin/Discord-Ticketing-Bot/issues) to avoid duplicates.
2.  **Open a New Issue:** If you don't find an existing report, open a new issue describing the problem.
3.  **Provide Clear and Concise Details:** Include the following information:
    * **Title:** A brief and descriptive title for the bug.
    * **Steps to Reproduce:** The exact steps you took to trigger the bug.
    * **Current Behavior:** What actually happened.
    * **Expected Behavior:** What you expected to happen.
    * **Environment Information:** Operating system, Python version, `discord.py` library version (if relevant).
    * Any relevant screenshots or logs that can help understand the issue.

## Requesting New Features (Feature Requests)

If you have an idea for a new feature, please follow these steps:

1.  **Check for Existing Requests:** Search the [open issues](https://github.com/K0lin/Discord-Ticketing-Bot/issues) for similar requests.
2.  **Open a New Issue:** If you don't find a similar request, open a new issue describing your idea.
3.  **Provide Clear and Concise Details:** Include the following information:
    * **Title:** A brief and descriptive title for the feature.
    * **Description:** A detailed explanation of what the feature should do.
    * **Motivation:** Why you think this feature is useful and what problem it would solve.
    * Potential benefits for users.
    * Any initial ideas on how it could be implemented.

## Contributing Code (Pull Requests)

We welcome code contributions! Please follow these steps:

1.  **Fork the Repository:** Click the "Fork" button at the top of the GitHub repository page.
2.  **Create a Branch:** Create a new branch from the `main` branch (or the designated development branch) for your changes. Give your branch a descriptive name (e.g., `fix-bug`, `add-ticket-close-command`).
    ```bash
    git checkout -b your-branch-name
    ```
3.  **Implement Your Changes:** Write the code to fix the bug or implement the feature.
4.  **Follow Coding Guidelines:**
    * Maintain a code style consistent with the rest of the project (generally adhering to PEP 8 for Python).
    * Write clear and well-commented code.
    * Include unit tests for new features or bug fixes (see the Testing section).
5.  **Update Documentation:** If your changes introduce new features or alter existing behavior, ensure you update the documentation accordingly.
6.  **Run Tests:** Ensure all tests pass. If you add new features, write new tests to verify them.
    ```bash
    # Example (into the next commit)
    pytest
    ```
7.  **Format Your Code:** Before submitting a pull request, format your code using a tool like `black` or `autopep8`.
    ```bash
    # into the next commit
    pip install black
    black .
    ```
8.  **Commit Your Changes:** Write clear and meaningful commit messages. Follow common commit message conventions (e.g., "feat: Add X feature", "fix: Resolve Y bug").
    ```bash
    git add .
    git commit -m "type: Short description of the change"
    ```
9.  **Push to Your Fork:** Push your branch to your forked repository on GitHub.
    ```bash
    git push origin your-branch-name
    ```
10. **Create a Pull Request:** From your forked repository page on GitHub, click the "Contribute" button and then "Open pull request".
11. **Describe Your Pull Request:** Provide a clear title and a detailed description of your changes, including the motivation and what your PR resolves or adds. Reference relevant issues using `#issue-number`.

## Testing

Including tests is crucial for ensuring the stability and reliability of the bot.

* **Unit Tests:** Write unit tests to verify the logic of individual functions and classes.
* **Integration Tests:** If your changes involve interaction between different parts of the bot or with the Discord API, consider writing integration tests as well.
* Follow the existing testing structure within the project. If no tests exist, we strongly encourage adding tests with your contributions.
* Ensure all tests pass before submitting your pull request.

## Documentation

Keeping the documentation up-to-date is essential.

* If you add new features, clearly describe them in the documentation.
* If you modify existing behavior, update the documentation accordingly.
* Pay attention to clarity and completeness in the documentation.

## Contributor Covenant Code of Conduct

We are committed to fostering an open and welcoming environment. We ask that you please review and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md) in all interactions within the project.

## 📄 License

This project is licensed under a Custom Restricted License - see the [LICENSE.md](LICENSE.md) file for details.

**Key Restrictions:**
- No distribution or redistribution allowed
- No sublicensing permitted
- No usage for illegal activities or purposes
- No commercial use without explicit permission

For permission requests or questions about licensing, please contact me into an issue.

⚠️ **Note:** Using this software for illegal purposes or in violation of Discord's Terms of Service is strictly prohibited.

---

## 📞 Support

If you encounter any issues or have questions, please open an [issue](https://github.com/K0lin/Discord-Ticketing-Bot/issues) on GitHub or contact the maintainer.

![Made with Python](https://forthebadge.com/images/badges/made-with-python.svg)
