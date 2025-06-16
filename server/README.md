Hello! You crash landed on the server side!

### Prerequisites

1. Make sure you actually have Go installed

```cmd
go --version
```

2. Install the dependences

```bash
go mod tidy

#or force installation
go mod download

```

3. Run the CompileDaemon

If you don't have GNU make (Recommended)

```bash
cd ./server/[server] #navigate to directory

# You need to at least have compile Daemon installed
CompileDaemon
```

Without the Daemon

```bash
cd ./server/[server]
go run main.go
```
