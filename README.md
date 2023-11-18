# supervisor-stdlog

A simple [supervisord](http://supervisord.org/) event listener to relay
process **stdout** _and_ **stderr** to supervisor's stdout.

This is useful in situations where supervisor oversees processes in a container / stack,  
so the logs can be collected by the orchestating runtime.

## Installation

Just install via pip

```shell
pip install supervisor-stdlog
```
...or add to your requirements.txt:

```ini
supervisor-stdlog==0.7.9
```

## Usage

An example supervisord.conf:

```ini
[supervisord]
nodaemon = true

[program:web]
command = ...
stdout_events_enabled = true
stderr_events_enabled = true

[eventlistener:stdlog]
events = PROCESS_LOG
command = supervisor-stdlog
result_handler = supervisor_stdlog:log_handler
buffer_size = 100
```
