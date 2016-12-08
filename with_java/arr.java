
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.HashMap;
import java.io.*;
import java.util.*;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;

public class arr 
{ public static int count=0;  
  public static HashSet<String> macset1=new HashSet<String>();
  public static HashSet<String> ipset1=new HashSet<String>();
  public static HashSet<String> protocol=new HashSet<String>();
  public static  HashMap<Integer, HashMap<String, String>> outerMap = new HashMap<Integer, HashMap<String,String>>();
  public static HashMap<String, String> innerMap;
  public static HashMap<String,String> mac_ip=new HashMap<String,String>();
  public static  HashMap<String, HashMap<String, Integer>> outerMap2 = new HashMap<String, HashMap<String,Integer>>();
  public static HashMap<String, Integer> innerMap2 ;
  
	public static void main(String[] args) 
	{ long startTime = System.currentTimeMillis();
		String csvFile = "/home/amit/project/with_java/test.csv";
		BufferedReader br = null;
		String line = "";
		String cvsSplitBy = ",";
		arr obj=new arr();
		obj.read();
		obj.protocol_count();
		obj.connected_comp();
		obj.bandwidth();
		obj.protocol_count_display();
		obj.protocol_capture();
		//System.out.println("overal map"+outerMap);
		System.out.println("MAc set"+macset1);
		System.out.println("Ip set"+ipset1);
		System.out.println("mac-ip set"+mac_ip);
		System.out.println("protocol set set"+protocol);
		System.out.println("no of protocol set "+protocol.size());
		System.out.println("No of computer connected "+mac_ip.size());
		//System.out.println("mac_protocol set"+outerMap2);
		System.out.println("mac_protocol set size "+outerMap2.size());
		Set s1=outerMap2.entrySet();
		System.out.println("outerMap "+s1);
        Iterator it = outerMap2.entrySet().iterator();
        //System.out.println("percentage ------------------"+(float)((60*100)/100));
        while(it.hasNext())
        {
            Map.Entry me = (Map.Entry)it.next();
            System.out.println("MAc: [" + me.getKey() + "], : [" + me.getValue() + "]");
        }
       // Set keyset=outerMap.keySet();
        
        // check key set values
        //System.out.println("Key set values are: " + keyset);
       

        
        long stopTime = System.currentTimeMillis();
        long elapsedTime = stopTime - startTime;
	  obj.time_execution(elapsedTime);
        System.out.println("total time elapsed"+elapsedTime+"mili seconds");
		
	}
	public  void read()
	{
		String csvFile = "/home/amit/project/with_java/test.csv";
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
					if(i==12)innerMap.put("ip_hostarp_src_proto_ipv4",datasets[i]); 
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
	

	public void protocol_count()
	{
	String[] mac = macset1.toArray( new String[0] );
	String[] proto = protocol.toArray( new String[0] );
	/*for(int j=0;j<proto.length;j++)
	{
		System.out.println(j+")"+proto[j]);
	}*/
	for(int i=0;i<mac.length;i++)
	{   innerMap2 = new HashMap<String, Integer>();
		for(int j=0;j<proto.length;j++)
		{
			if(proto[j].length()>50)
			{
				innerMap2.put(proto[j].substring(0,25), 0);
			}
		    else if(proto[j].length()<14){}
		    else
		    {
		    	innerMap2.put(proto[j], 0);
		    }
		}
		innerMap2.put("frame_len",0);
		outerMap2.put(mac[i], innerMap2);
	}
	
	for(int i=0;i<mac.length;i++)
	{innerMap2 = new HashMap<String, Integer>();
		Iterator iterator = outerMap.keySet().iterator();
	    while (iterator.hasNext()) 
	    {
	      int j = (int)iterator.next();
	      
	 
		try{
		if(mac[i].equalsIgnoreCase(outerMap.get(j).get("ETH_SRC").toString()))
		{
		  if(outerMap.get(j).containsKey("frame_len"))
		  {
			 int len=outerMap2.get(mac[i]).get("frame_len");
			 int len2=Integer.parseInt( outerMap.get(j).get("frame_len"));
			 innerMap2.put("frame_len", len2+len);
		  }
		 if(outerMap.get(j).containsKey("frame_protocols"))
		  {   String proto1=outerMap.get(j).get("frame_protocols").toString();
		      //System.out.println(proto1);
		      if(outerMap2.get(mac[i]).containsKey(proto1))
		      {//System.out.println("contains"+proto1);
			  int len=outerMap2.get(mac[i]).get(proto1);
			  innerMap2.put(outerMap.get(j).get("frame_protocols"),len+1); 
		      }
		      else
		      {//System.out.println("doesn't contains"+proto1);
		    	  if(proto1.length()>50)
					{
						innerMap2.put(proto1.substring(0,25), 0);
					}
				    else
				    {
				    	innerMap2.put(proto1, 0);
				    }
		    	  
		    	  
		      }
		  }
		
		outerMap2.put(mac[i], innerMap2);
		}}
		catch(NullPointerException e){}
	
	}
	    
	}



		
	}
	
	public void connected_comp()
	{
		try {

			String content = "";

			File file = new File("/home/amit/project/with_java/conn_comp.txt");
					System.out.println("mac-ip set"+mac_ip);
			// if file doesnt exists, then create it
			if (!file.exists()) {
				file.createNewFile();
			}

			FileWriter fw = new FileWriter(file.getAbsoluteFile());
			BufferedWriter bw = new BufferedWriter(fw);
			 Iterator it = mac_ip.entrySet().iterator();

		        while(it.hasNext())
		        {
		            Map.Entry me = (Map.Entry)it.next();
		           content="Mac: [" + me.getKey() + "],Associated  ip: [" + me.getValue() + "]\n";
		           bw.write(content);
		        }
		        content="Total number of computer connected"+mac_ip.size();
			bw.write(content);
			bw.close();

			System.out.println("Done");

		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	public void bandwidth()
	{
		try {

			String content = "";

			File file = new File("/home/amit/project/with_java/bandwidth.txt");

			// if file doesnt exists, then create it
			if (!file.exists()) {
				file.createNewFile();
			}
			HashMap<String,Float> band=new HashMap<String,Float>();
			float total_length=0;
			float each_length=0;
			float per=0;
			Iterator iterator = outerMap2.keySet().iterator();
			while (iterator.hasNext()) 
		    {
		      String key = (String)iterator.next();
		      total_length=outerMap2.get(key).get("frame_len");
		    }
			Iterator iterator2 = outerMap2.keySet().iterator();
			while (iterator2.hasNext()) 
		    {
		      String key = (String)iterator2.next();
		      each_length=outerMap2.get(key).get("frame_len");
		     // System.out.println("each_length"+each_length);
		      per=(float)((each_length)/total_length);
		      
		     // System.out.println("percentage"+per);
		      band.put(key, per);
		    }
			//System.out.println("bandwidth set total length"+total_length);
			System.out.println("bandwidth set"+band);
			
			FileWriter fw = new FileWriter(file.getAbsoluteFile());
			BufferedWriter bw = new BufferedWriter(fw);
		       content="Total number of packet capture "+outerMap.size()+"\n";
				bw.write(content);
			 Iterator it = band.entrySet().iterator();

		        while(it.hasNext())
		        {
		            Map.Entry me = (Map.Entry)it.next();
		           content="Mac: [" + me.getKey() + "]          bandwidth per%: [" + me.getValue() + "]\n";
		           bw.write(content);
		        }
		 
			bw.close();

			System.out.println("Done");

		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}
	public void protocol_count_display()
	{
		try {

			String content = "";

			File file = new File("/home/amit/project/with_java/protocol_count_display.txt");

			// if file doesnt exists, then create it
			if (!file.exists()) {
				file.createNewFile();
			}

			FileWriter fw = new FileWriter(file.getAbsoluteFile());
			BufferedWriter bw = new BufferedWriter(fw);
			 Iterator it = outerMap2.entrySet().iterator();

		        while(it.hasNext())
		        {
		            Map.Entry me = (Map.Entry)it.next();
		           content="\nMac: [" + me.getKey() + "]\n\t,[" + me.getValue() + "]\n\t";
		           bw.write(content);
		        }
			
			bw.close();

			System.out.println("Done");

		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	public void time_execution(long time)
	{

		try {

			String content = "";

			File file = new File("/home/amit/project/with_java/execution_time.txt");

			// if file doesnt exists, then create it
			if (!file.exists()) {
				file.createNewFile();
			}

			FileWriter fw = new FileWriter(file.getAbsoluteFile());
			BufferedWriter bw = new BufferedWriter(fw);
			
			 
		        content=time+" ";
			content.trim();
			bw.write(content);
			
			bw.close();

			System.out.println("Done");

		} catch (IOException e) {
			e.printStackTrace();
		}
	
	
		
	}

	public void protocol_capture()
	{
		try {

			String content = "";

			File file = new File("/home/amit/project/with_java/protocol_capture.txt");
			int count=1;

			// if file doesnt exists, then create it
			if (!file.exists()) {
				file.createNewFile();
			}

			FileWriter fw = new FileWriter(file.getAbsoluteFile());
			BufferedWriter bw = new BufferedWriter(fw);
			
			 Iterator<String> it = protocol.iterator();
		     while(it.hasNext())
		     {
		        content="\n"+count+")."+it.next()+"\n";
			bw.write(content);
			count++;
			}
			bw.close();

			System.out.println("Done");

		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
}
