import sys
import asyncio
import configparser
from aiopjlink.projector import PJLink, PJClass

CONFIG_FILE = "cli2.config"

def load_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    section = config["projector"]
    return section["ip"], section["password"], float(section.get("timeout", 4))

async def main():
    if len(sys.argv) < 2:
        print("Usage: python cli2.py <command> [args...]")
        print("Example: python cli2.py power_on")
        sys.exit(1)

    ip, password, timeout = load_config()
    cmd = sys.argv[1].lower()
    args = sys.argv[2:]

    async with PJLink(address=ip, password=password, timeout=timeout) as pj:
        # Power
        if cmd == "power_on":
            await pj.power.turn_on()
            print("Power ON")
        elif cmd == "power_off":
            await pj.power.turn_off()
            print("Power OFF")
        elif cmd == "power_status":
            print("Power status:", await pj.power.get())

        # Sources
        elif cmd == "get_source":
            print("Current source:", await pj.sources.get())
        elif cmd == "set_source":
            if len(args) != 2:
                print("Usage: set_source <mode> <index>")
                sys.exit(1)
            print("Set source:", await pj.sources.set(args[0], args[1]))
        elif cmd == "list_sources":
            print("Available sources:", await pj.sources.available())
        elif cmd == "list_sources_with_names":
            print("Available sources with names:", await pj.sources.available_with_names())
        elif cmd == "source_resolution":
            print("Current resolution:", await pj.sources.resolution())
        elif cmd == "recommended_resolution":
            print("Recommended resolution:", await pj.sources.recommended_resolution())

        # Mute
        elif cmd == "mute_status":
            print("Mute status (video, audio):", await pj.mute.status())
        elif cmd == "mute_video":
            await pj.mute.video(True)
            print("Video muted")
        elif cmd == "unmute_video":
            await pj.mute.video(False)
            print("Video unmuted")
        elif cmd == "mute_audio":
            await pj.mute.audio(True)
            print("Audio muted")
        elif cmd == "unmute_audio":
            await pj.mute.audio(False)
            print("Audio unmuted")
        elif cmd == "mute_both":
            await pj.mute.both(True)
            print("Both muted")
        elif cmd == "unmute_both":
            await pj.mute.both(False)
            print("Both unmuted")

        # Errors
        elif cmd == "errors":
            print("Errors:", await pj.errors.query())

        # Lamp
        elif cmd == "lamp_status":
            print("Lamp status:", await pj.lamps.status())
        elif cmd == "lamp_hours":
            print("Lamp hours:", await pj.lamps.hours())
        elif cmd == "lamp_models":
            print("Lamp replacement models:", await pj.lamps.replacement_models())

        # Filter
        elif cmd == "filter_hours":
            print("Filter hours:", await pj.filter.hours())
        elif cmd == "filter_models":
            print("Filter replacement models:", await pj.filter.replacement_models())

        # Freeze
        elif cmd == "freeze":
            await pj.freeze.set(True)
            print("Freeze ON")
        elif cmd == "unfreeze":
            await pj.freeze.set(False)
            print("Freeze OFF")
        elif cmd == "freeze_status":
            print("Freeze status:", await pj.freeze.get())

        # Volume
        elif cmd == "mic_up":
            await pj.microphone.turn_up()
            print("Microphone volume up")
        elif cmd == "mic_down":
            await pj.microphone.turn_down()
            print("Microphone volume down")
        elif cmd == "spk_up":
            await pj.speaker.turn_up()
            print("Speaker volume up")
        elif cmd == "spk_down":
            await pj.speaker.turn_down()
            print("Speaker volume down")

        # Information
        elif cmd == "info":
            print("Projector info:", await pj.info.table())
        elif cmd == "software_version":
            print("Software version:", await pj.info.software_version())
        elif cmd == "serial_number":
            print("Serial number:", await pj.info.serial_number())
        elif cmd == "pjlink_class":
            print("PJLink class:", await pj.info.pjlink_class())
        elif cmd == "other_info":
            print("Other info:", await pj.info.other())
        elif cmd == "product_name":
            print("Product name:", await pj.info.product_name())
        elif cmd == "manufacturer_name":
            print("Manufacturer name:", await pj.info.manufacturer_name())
        elif cmd == "projector_name":
            print("Projector name:", await pj.info.projector_name())
        else:
            print(f"Unknown command: {cmd}")
            sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())