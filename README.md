# SSHoney - SSH Honeypot with Paramiko

## Overview

This Python script sets up a simple SSH honeypot using the Paramiko library. The honeypot logs authentication attempts for both password and public key-based logins.

## Features

- Logs username and password combinations for failed password-based authentication.
- Logs username and public key pairs for failed public key-based authentication.
- Multithreaded to handle multiple connection attempts simultaneously.
- Uses the Paramiko library for SSH functionality.

## Prerequisites

- Python 3.x
- Paramiko library

## Installation

1. Install the required library using the following command:

    ```bash
    pip install paramiko
    ```

2. Run the script:

    ```bash
    python honeypot.py
    ```

## Configuration

- The script binds to `0.0.0.0:22` by default. You can modify the script to change the listening address and port.

## License

See the [LICENSE.md](LICENSE.md) file for details.

## Author

- Hex

