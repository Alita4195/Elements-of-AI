def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    # https://sea-distances.org/
    # nautical miles converted to km
    routes = []
    port1 = 0
    for port2 in range(1, 5):
        # print (port2) 
        for port3 in range(1, 5):
            # print(port3)
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]

                    if port1 != port2 and port1 != port3 and port1 != port4 and port1 != port5 and port2 != port3 and port2 != port4 and port2 != port5 and port3 != port4 and port3 != port5 and port4 != port5:
                        # print(route)
                        # print(portnames[port1],portnames[port2],portnames[port3],portnames[port4],portnames[port5])

                    #     # do not modify this print statement
                        # route_array=(' '.join([portnames[i] for i in route]))
                        routes.append(route)
    print(routes)

    D = [
            [0,8943,8019,3652,10545],
            [8943,0,2619,6317,2078],
            [8019,2619,0,5836,4939],
            [3652,6317,5836,0,7825],
            [10545,2078,4939,7825,0]
        ]

    # https://timeforchange.org/co2-emissions-shipping-goods
    # assume 20g per km per metric ton (of pineapples)


    co2 = 0.020

    # route = [0, 1, 2, 3, 4]
    for r in routes:
        distance = D[r[0]][r[1]] + D[r[1]][r[2]] + D[r[2]][r[3]] + D[r[3]][r[4]]
        emissions = distance * co2
        print(' '.join([portnames[i] for i in r]) + " %.1f kg" % emissions)
    
main()