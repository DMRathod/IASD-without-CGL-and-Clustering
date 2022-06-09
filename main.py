import time
import Initialize

if __name__ == '__main__':

    source_coordinates = (11, 59)
    destination_coordinates = (39, 41)

    # $$ Initilize nodes $$
    list_of_all_nodes = Initialize.Init_nodes()

    # request with source, destination and intent where we have considered
    # intent = 1 for fuel station,
    # intent = 2 for restaurant

    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%--First Case--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    start_time = time.time()
    list_of_all_nodes[0].service_request(source_coordinates, destination_coordinates, intent=1)
    total_time = (time.time() - start_time)*1000
    print("--- %s milli-seconds taken to execute ---" % (total_time))
    print()

    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%--Second Case--%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    start_time = time.time()
    list_of_all_nodes[0].service_request(source_coordinates, destination_coordinates, intent=2)
    total_time = (time.time() - start_time)*1000
    print("--- %s milli-seconds taken to execute ---" % (total_time))
    print()


