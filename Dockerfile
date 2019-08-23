FROM python:3

COPY entrypoint.py /entrypoint

ENTRYPOINT ["/entrypoint"]
CMD []
