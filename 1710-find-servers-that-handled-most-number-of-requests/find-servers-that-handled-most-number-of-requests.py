class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available_servers = SortedList(range(k))
        busy_servers = []
        request_count = [0] * k
      
        for request_id, (arrival_time, processing_time) in enumerate(zip(arrival, load)):
            while busy_servers and busy_servers[0][0] <= arrival_time:
                end_time, server_id = heappop(busy_servers)
                available_servers.add(server_id)
          
            if not available_servers:
                continue
   
            target_server = request_id % k
            server_index = available_servers.bisect_left(target_server)
          
            # If no server >= target_server exists, wrap around to the first server
            if server_index == len(available_servers):
                server_index = 0
          
            # Assign the request to the selected server
            selected_server = available_servers[server_index]
            request_count[selected_server] += 1
          
            heappush(busy_servers, (arrival_time + processing_time, selected_server))
            available_servers.remove(selected_server)
      
        max_requests = max(request_count)
        return [server_id for server_id, count in enumerate(request_count) if count == max_requests]
