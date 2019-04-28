# Simple Message Oriented Relay

Stupid simple way to relay messages between two programs.

# Client usage

Import and configure on both clients:

```py
import smor.client as sm
# ...
sm.config('www.example.com')

# or sm.config(host, port)
# port defaults to 8085
```

Now lets send some data! Sending and receiving is mailbox oriented, so we need to choose a mailbox name (e.g. `'box'`)

```py
sm.put('box', 'Hello!')
```

And on some other end, receive that data! We use the same mailbox name.

```py
print(sm.get_one('box')) # Prints `Hello!` (or `None`, if message wasn't sent yet)
```

We can also get all waiting messages with `get_all(msgbox)`. This returns a list of all messages waiting to be received.

```py
print(sm.get_all('box'))
```

Dead simple indeed. Getting never waits for messages, `None` is returned whenever no messages are available. Each message is deleted when received (`get_all` deletes all messages).

**NOTE:** intended for 1-on-1 communication, trying to `get` from multiple endpoints (machines, processes, threads) may skip some messages. `put`ting from multiple endpoints should be fine though.

# Server usage

## Starting the server

```sh
python -m smor.server host=0.0.0.0 port=8085
```

You can skip either host or port argument to keep defaults.

## Stopping the server

Ctrl-C it. Did you really think I made a fancier solution? Messages on server are not persisted, so stopping the server will lose all remaining messages.