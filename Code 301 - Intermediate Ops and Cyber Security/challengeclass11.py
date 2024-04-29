# Script Name:                  Ops Challenge - Python File Handling
# Author:                       Gilbert Collado
# Date of latest revision:      04/08/2024
# Purpose:                      Create a script that uses file handling in python
# Source1:                      https://github.com/codefellows/seattle-ops-301d12/tree/main/class-10/challenges
# Source2:                      https://g.co/gemini/share/6514345f86aa
import psutil

def get_system_info():
    cpu_times = psutil.cpu_times()

    # Time spent by normal processes executing in user mode
    user_mode_time = cpu_times.user

    # Time spent by processes executing in kernel mode
    kernel_mode_time = cpu_times.system

    # Time when system was idle
    idle_time = cpu_times.idle

    # Time spent by priority processes executing in user mode
    priority_user_time = cpu_times.nice

    # Time spent waiting for I/O to complete
    io_wait_time = cpu_times.iowait

    # Time spent for servicing hardware interrupts
    hardware_interrupt_time = cpu_times.irq

    # Time spent for servicing software interrupts
    software_interrupt_time = cpu_times.softirq

    # Time spent by other operating systems running in a virtualized environment
    steal_time = cpu_times.steal

    # Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
    guest_time = cpu_times.guest

    # Print the obtained information
    print("Time spent by normal processes executing in user mode:", user_mode_time)
    print("Time spent by processes executing in kernel mode:", kernel_mode_time)
    print("Time when system was idle:", idle_time)
    print("Time spent by priority processes executing in user mode:", priority_user_time)
    print("Time spent waiting for I/O to complete:", io_wait_time)
    print("Time spent for servicing hardware interrupts:", hardware_interrupt_time)
    print("Time spent for servicing software interrupts:", software_interrupt_time)
    print("Time spent by other operating systems running in a virtualized environment:", steal_time)
    print("Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel:", guest_time)

if __name__ == "__main__":
    get_system_info()

