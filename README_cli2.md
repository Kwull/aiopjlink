# README_cli2.md

## PJLink CLI2 Console Application

`cli2.py` is a command-line tool for controlling and querying projectors using the PJLink protocol. It supports all available commands from the PJLink library and reads connection parameters from a configuration file.

---

## Configuration

Before using `cli2.py`, create a `cli2.config` file in the same directory with the following content:

```ini
[projector]
ip = 192.168.68.124
password = 1234
timeout = 4
```

- `ip`: Projector IP address
- `password`: PJLink password (if required)
- `timeout`: Connection timeout in seconds (default: 4)

---

## Usage

Run the CLI with:

```sh
python cli2.py <command> [args...]
```

- Only one command can be executed per run.
- Some commands require additional arguments.

---

## Examples

### Power On the Projector

```sh
python cli2.py power_on
```

### Power Off the Projector

```sh
python cli2.py power_off
```

### Query Power Status

```sh
python cli2.py power_status
```

### Set Input Source

```sh
python cli2.py set_source rgb 1
```

### Get Current Source

```sh
python cli2.py get_source
```

### Query Errors

```sh
python cli2.py errors
```

### Get Projector Information

```sh
python cli2.py info
```

---

## Supported Commands

- `power_on`, `power_off`, `power_status`
- `get_source`, `set_source <mode> <index>`, `list_sources`, `list_sources_with_names`
- `source_resolution`, `recommended_resolution`
- `mute_status`, `mute_video`, `unmute_video`, `mute_audio`, `unmute_audio`, `mute_both`, `unmute_both`
- `errors`
- `lamp_status`, `lamp_hours`, `lamp_models`
- `filter_hours`, `filter_models`
- `freeze`, `unfreeze`, `freeze_status`
- `mic_up`, `mic_down`, `spk_up`, `spk_down`
- `info`, `software_version`, `serial_number`, `pjlink_class`, `other_info`, `product_name`, `manufacturer_name`, `projector_name`

---

## Notes

- Make sure your projector supports the PJLink protocol and is accessible from your network.
- The CLI will print usage instructions if you run it without arguments or with an unknown command.

---