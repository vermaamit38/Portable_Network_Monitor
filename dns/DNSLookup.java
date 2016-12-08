//package dns;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.io.*;
import java.util.*;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;

import javax.naming.directory.Attributes;
import javax.naming.directory.InitialDirContext;
import javax.naming.NamingEnumeration;
import javax.naming.NamingException;

import java.net.InetAddress;
import java.net.UnknownHostException;

public class DNSLookup 
{
	public static int count=0;  
	//public static int count=0;  
	  public static HashMap<String,String> mac_ip=new HashMap<String,String>();
	  public static HashSet<String> macset1=new HashSet<String>();
	  public static HashSet<String> ipset1=new HashSet<String>();
	  public static HashSet<String> protocol=new HashSet<String>();
	  public static  HashMap<Integer, HashMap<String, String>> outerMap = new HashMap<Integer, HashMap<String,String>>();
	  public static HashMap<String, String> innerMap;
	  public static HashMap<String,HashSet<String>> dns=new HashMap<String,HashSet<String>>();
	  public static HashSet<String> dns_set;

	public static void main(String[] args) 
	{
		DNSLookup obj=new DNSLookup();
		obj.read();
		obj.dns_set();
		obj.dns_resolve();
		Iterator it = dns.entrySet().iterator();
        //System.out.println("percentage ------------------"+(float)((60*100)/100));
        while(it.hasNext())
        {
            Map.Entry me = (Map.Entry)it.next();
            System.out.println("MAC: [" + me.getKey() + "], : [" + me.getValue() + "]");
        }

	}
	public  void read()
	{
		String csvFile = "/home/amit/project/dns/test1212.csv";
		BufferedReader br = null;
		String line = "";
		String cvsSplitBy = ",";
        int count=0;
      
		try {
          
			br = new BufferedReader(new FileReader(csvFile));
			while (((line = br.readLine()) != null) ) 
			{
			 String[] datasets = line.split(cvsSplitBy);
			   if(count>0 )
			   {	innerMap= new HashMap<String, String>();
				  // System.out.println(line);
					for(int i=0;i<datasets.length;i++)
				     {if(datasets[i].length()>2)
				       {if(datasets[i].startsWith("\"") && datasets[i].endsWith("\""))
				    	 datasets[i]=datasets[i].substring(1,datasets[i].length()-1);
				       }
					if(i==0)innerMap.put("frame_number",datasets[i]);
					if(i==1)innerMap.put("frame_time",datasets[i]); 
					if(i==3)innerMap.put("frame_time_relative",datasets[i]); 
					if(i==4)innerMap.put("frame_len",datasets[i]); 
					if(i==5)
					{
						innerMap.put("frame_protocols",datasets[i]);
					protocol.add(datasets[i]);
					} 
					if(i==6)
					{
						innerMap.put("ETH_SRC",datasets[i]); 
					macset1.add(datasets[i]);
					}
					if(i==7)innerMap.put("ETH_DST",datasets[i]); 
					if(i==8)
					{innerMap.put("IP_SRC",datasets[i]);
				        ipset1.add(datasets[i]);
				        mac_ip.put(datasets[6],datasets[8]);
				     }
					if(i==9)innerMap.put("IP_DST",datasets[i]); 
					if(i==10)innerMap.put("IP_Protocol",datasets[i]);  
					if(i==11)innerMap.put("ip_ttl",datasets[i]); 
					if(i==12)innerMap.put("ip_host",datasets[i]); 
					if(i==13)innerMap.put("arp_src_proto_ipv4",datasets[i]);  
					if(i==14)innerMap.put("arp_dst_proto_ipv4",datasets[i]); 
					if(i==15)innerMap.put("http_request_method",datasets[i]); 
					if(i==16)innerMap.put("http_request_uri",datasets[i]);  
					if(i==17)innerMap.put("http_host",datasets[i]);
					//System.out.println("innermap"+innerMap);
					outerMap.put(count, innerMap);
					
					//System.out.println("outermap"+outerMap);
					}
					}count++;
			}

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if (br != null) {
				try {
					br.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}


	}
	public void dns_set()
	{
		String[] mac = macset1.toArray( new String[0] );
		String[] proto = protocol.toArray( new String[0] );
		/*for(int j=0;j<proto.length;j++)
		{
			System.out.println(j+")"+proto[j]);
		}*/
		for(int i=0;i<mac.length;i++)
		{   dns_set=new HashSet<String>();
			
			dns.put(mac[i], dns_set);
		}
		int coun=0;
		for(int i=0;i<mac.length;i++)
		{coun=0;
			dns_set=new HashSet<String>();
			Iterator iterator = outerMap.keySet().iterator();
		    while (iterator.hasNext()) 
		    {
		      int j = (int)iterator.next();
			  try
			   {
			   if(mac[i].equalsIgnoreCase(outerMap.get(j).get("ETH_SRC").toString()))
			    {
			          if(outerMap.get(j).containsKey("IP_DST"))
			            {coun++;
			        	  String ips= outerMap.get(j).get("IP_DST").toString();
			        	 // System.out.print(ips+" ,");
			        	  if(!ips.startsWith("192."))
			        		  dns_set.add(ips);
			        	 
			             }
			         
			     }
			   }
			   catch(NullPointerException e){}
		    }dns.put(mac[i],dns_set);
		    //System.out.print(dns_set);
		    //System.out.println("number of ip_host found at mac:"+mac[i]+" is "+coun);
		    
		}
		
	}
   public void dns_resolve()
    {  long startTime=System.currentTimeMillis();
    try {

		String content = "";

		File file = new File("/home/amit/project/with_java/dns.txt");
				System.out.println("mac-ip set"+mac_ip);
		// if file doesnt exists, then create it
		if (!file.exists()) {
			file.createNewFile();
		}

		FileWriter fw = new FileWriter(file.getAbsoluteFile());
		BufferedWriter bw = new BufferedWriter(fw);
		
		
		//-----------normal execution for inner try and outer try for filewrite
	  // Map<String, HashSet<String>> remarksMap = new HashMap<String, HashSet<String>>();
	   for (String k: dns.keySet()) {
		    System.out.println("\n\n\n\nfor mac "+k+" -----------------------------------------------------------------------");
		    String data1="\n-------------------"+k+"----------------------------\n";
		    bw.write(data1);
		    for (String v: dns.get(k))
		    {data1="";
		        System.out.println("Resolve for ip:"+v);
		        data1="\t"+v+"\t:";
		        
		
    	 try
         {
             InetAddress inetAddress;
             // if first character is a digit then assume is an address
             if(v.length()>0)
             {
             if (Character.isDigit(v.charAt(0)))
             {   // convert address from string representation to byte array
                 byte[] b = new byte[4];
                 String[] bytes = v.split("[.]");
                 for (int i = 0; i < bytes.length; i++)
                 {
                     b[i] = new Integer(bytes[i]).byteValue();
                 }
                 // get Internet Address of this host address
                 inetAddress = InetAddress.getByAddress(b);
             }
             else
             {   // get Internet Address of this host name
                 inetAddress = InetAddress.getByName(v);
             }
             // show the Internet Address as name/address
             System.out.println(inetAddress.getHostName()) ;
             data1+=inetAddress.getHostName()+"\n";
             bw.write(data1);
             //System.out.println("/" + inetAddress.getHostAddress());
             // get the default initial Directory Context
             InitialDirContext iDirC = new InitialDirContext();
             // get the DNS records for inetAddress
             Attributes attributes = iDirC.getAttributes("dns:/" + inetAddress.getHostName());
             // get an enumeration of the attributes and print them out
             NamingEnumeration attributeEnumeration = attributes.getAll();
             //System.out.println("-- DNS INFORMATION --");
             while (attributeEnumeration.hasMore())
             {
                attributeEnumeration.next();
             }
             attributeEnumeration.close();
         }
         }
         catch (UnknownHostException exception)
         {
             //System.err.println("ERROR: No Internet Address for " + v );
         }
         catch (NamingException exception)
         {
             //System.err.println("ERROR: No DNS record for " + v );
         }
		    }
	   }
	   bw.close();

		System.out.println("Done");

	} catch (IOException e) {
		e.printStackTrace();
	}

	   long stopTime = System.currentTimeMillis();
       long elapsedTime = stopTime - startTime;
       System.out.println("It took  "+elapsedTime+" mili seconds");
  
    }

}
