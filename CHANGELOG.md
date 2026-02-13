# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-02-10

### Added
- Initial release of text-humanizer
- Core functionality to analyze text readability
- Humanity Score calculation based on Flesch Reading Ease
- Beautiful terminal UI with Rich library
- Support for Markdown (.md) and plain text (.txt) files
- AI shame word detection (delve, testament, tapestry, etc.)
- CLI command `check-human`
- Stdin support for piping text
- Comprehensive test suite
- GitHub Actions CI/CD pipeline

### Features
- Flesch Reading Ease score calculation
- Average sentence length analysis
- Color-coded gauge visualization (Robot to Human)
- Detailed metrics table
- Verbose mode for additional information
- Cross-platform support (Windows, macOS, Linux)
