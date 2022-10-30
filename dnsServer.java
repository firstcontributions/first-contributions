
/// Java Application for simulation of DNS using UDP Sockets for retrieve ip address for any given domain name

import java.io.*;
import java.net.*;
import java.util.*;
import java.lang.ProcessBuilder;
import java.lang.String;

public class dnsServer
{
    public static void main(String args[])
    {
        try
        {
            DatagramSocket server=new DatagramSocket(1309);
            while(true)
            {
              byte[] sendbyte = new byte[1024];
              byte[] receivebyte = new byte[1024];
			   
              DatagramPacket receiver=new DatagramPacket(receivebyte,receivebyte.length);
              server.receive(receiver);
                                    
			  String str=new String(receiver.getData());
              String s = str.trim();
                                    
               Process process = Runtime.getRuntime().exec("ping "+s+" -n 1");
	           String ip = getResults(process,s);
			   
			   InetAddress addr= receiver.getAddress();
               int port=receiver.getPort();
			   
			   sendbyte = ip.getBytes();
               DatagramPacket sender = new DatagramPacket(sendbyte,sendbyte.length,addr,port);
               server.send(sender);
               break;
			   
	        }
	
	     }
    
        catch(Exception e)
        {
            System.out.println(e);
        }
    }
	
	 public static String getResults(Process process,String url) throws IOException 
       		 {
				 
				  BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
				  
			         String line = null;
					 String mesg = new String();
			
				  while (  (line = reader.readLine()) != null )  
				  {  
			            mesg += line;
					             // System.exit(0);
						  
				  }
				  
				  int si = mesg.indexOf("[");
				  int di = mesg.indexOf("]");
				  
				  String s1 = mesg.substring(si+1,di);
			
     			 return s1; 
			 }	
			
			
}