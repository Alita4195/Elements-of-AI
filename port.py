def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    port1 = 0
    for port2 in range(1, 5):
        # print (port2) 
        for port3 in range(1, 5):
            # print(port3)
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]
    # print(route)

                    # Modify this if statement to check if the route is valid
                    if port1 != port2 and port1 != port3 and port1 != port4 and port1 != port5 and port2 != port3 and port2 != port4 and port2 != port5 and port3 != port4 and port3 != port5 and port4 != port5:
                        # print(route)
                        # print(portnames[port1],portnames[port2],portnames[port3],portnames[port4],portnames[port5])

                    #     # do not modify this print statement
                        print(' '.join([portnames[i] for i in route]))

main()