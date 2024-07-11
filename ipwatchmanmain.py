#ipwatchmanmain.py
import sys
import time
from datetime import datetime
from PINGGing import ping_ip
from dabadase import add_ip_event
import concurrent.futures



def Ipwatchman(ip_address, packet_size=2, timeout=1,timepar=0):
      while True :
        result = ping_ip(ip_address, packet_size, timeout)
        print(f"Ping result for {ip_address}: {result}")
        
        if result != True:
          time.sleep(timepar)
          if ping_ip(ip_address, packet_size, timeout) != True:
            fail_time = datetime.now()
            print(f"Failed to ping {ip_address}. Sending email notification...")
            add_ip_event(ip_address=ip_address, event_type="Failure",date_ = datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            #send_email(subject, f'Failed to ping {ip_address}.', from_email, to_email, smtp_server, smtp_port, smtp_user, smtp_password)

            while ping_ip(ip_address, packet_size, timeout) != True:
                print("Ping failed. Waiting to recover...")
                time.sleep(timepar)  
            
            recovery_time = int((datetime.now() - fail_time).total_seconds())
            print(f"Email sent. {ip_address} is reachable after {recovery_time}")
            add_ip_event(ip_address=ip_address, event_type="Recovery",date_ = datetime.now().strftime("%Y-%m-%d %H:%M:%S"), recovery_time=recovery_time)
             #send_email(subject, f"Failed to ping {ip_address}.", from_email, to_email, smtp_server, smtp_port, smtp_user, smtp_password)
        
        


if __name__ == "__main__":
  
    ip_address = sys.argv[1]
    packet_size = int(sys.argv[2])
    timeout = int(sys.argv[3])
    
    Ipwatchman(ip_address, packet_size, timeout, timepar=0)
    
    
   
        

                                                                           
                                                                           
  
  



  


