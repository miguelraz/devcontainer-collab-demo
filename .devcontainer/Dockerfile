FROM mcr.microsoft.com/devcontainers/python:3.12

# Install uv — a fast Python package manager written in Rust
# https://github.com/astral-sh/uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Install Python scientific stack into the system interpreter.
# Done at build time so the resulting image is self-contained and
# does not depend on postCreateCommand succeeding.
RUN uv pip install --system numpy matplotlib
