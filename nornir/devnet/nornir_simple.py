from nornir.core import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


nr = InitNornir()

result = nr.run(
        task=netmiko_send_command,
        command_string="show interfaces"
)

print_result(result)
