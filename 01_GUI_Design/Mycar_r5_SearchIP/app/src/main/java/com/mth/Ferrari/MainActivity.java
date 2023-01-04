package com.mth.Ferrari;


import android.app.Activity;
import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.os.StrictMode;
import android.provider.ContactsContract;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private EditText ip;
    private String ip_address;
    private TextView myIPList;
    private String TAG = "MTH_Morgan";
    private String Str_text = "";

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ip = (EditText) findViewById(R.id.myIP);
        myIPList = (TextView)findViewById(R.id.myIPList);

    }


    public void SearchIP(View view) throws InterruptedException {
        myIPList.setText("");
        Str_text = "";
        ip_address = ip.getText().toString();
        Log.e("MTH_Morgan IP address 1", ip_address);

        if (ip_address.length() == 0) {
            ip_address = "192.168.0.x";
        }

        String target = ".";
        int count = 0;
        String ip_address_check = ip_address;
        while (ip_address_check.contains(target)) {
            ip_address_check = ip_address_check.substring(ip_address_check.indexOf(target) + 1);
            ++count;
        }


        if (count == 3) {
            if (ip_address.contains("x")) {
                for (int ip = 1; ip < 255; ip++) {
                    final int finalIp = ip;
//                    ping(finalIp);
                    new Thread(() -> ping(finalIp)).start();
                }


                Thread.sleep(5000);

                myIPList.setText(Str_text + "\n" + "Done");

            } else Toast.makeText(this, "pls click button OK", Toast.LENGTH_SHORT).show();
        } else Toast.makeText(MainActivity.this, "wrong IP format", Toast.LENGTH_LONG).show();
    }


    public void gotoMain(View view) {
        ip_address = ip.getText().toString();
        Log.e("MTH_Morgan IP address 1", ip_address);
        String target = ".";

        int count = 0;
        String ip_address_check = ip_address;
        while (ip_address_check.contains(target)) {
            ip_address_check = ip_address_check.substring(ip_address_check.indexOf(target) + 1);
            ++count;
        }


        if (ip_address.length() == 0) {
            ip_address = "192.168.0.x";
        }

        if (count == 3) {
            if (!ip_address.contains("x")) {
                Intent intent = null;
                switch (view.getId()) {
                    case R.id.Changepage:
                        try {
                            intent = new Intent(MainActivity.this, IPInput.class);
                            intent.putExtra("ip_address", ip_address);
//                    intent.putStringArrayListExtra("timestamp", timestamp);
                            startActivity(intent);
                        } catch (Exception e) {
                            Toast.makeText(MainActivity.this, "no intent", Toast.LENGTH_LONG).show();
                            Log.e("MTH_Morgan", e.toString());
                        }
                }
            }else Toast.makeText(this, " pls check the button SearchIP'", Toast.LENGTH_SHORT).show();
        }else Toast.makeText(MainActivity.this, "wrong IP format", Toast.LENGTH_LONG).show();
    }

    boolean ping(int i) {
        // 前缀根据自己需求调整
//        String ip = "10.11.39." + i;
        String str = ip_address.substring(0,ip_address.length()-1);
        String ins = "ping " + str + i;
//        Log.e("MTH_Morgan IP address x", ins);
        try {
            Process p = Runtime.getRuntime().exec(ins);
            BufferedReader reader = new BufferedReader(new InputStreamReader(p.getInputStream(), "GBK"));
            String line = null;
            while ((line = reader.readLine()) != null) {
                //System.out.println("line---"+line);
//                Log.e(TAG + "test line---"+ins, line);

                if (line.toLowerCase().contains("ttl=")) { //这里不同的cmd可能不一样 Reply from 10.11.39.2: bytes=32 time<1ms TTL=128
//                    System.out.println(ins + " 连接成功");
                    Log.e(TAG + "success connected to", ins);
                    Str_text = Str_text + "\n" + str + i;
                    return true;
                }
                if (line.toLowerCase().contains("unreachable")) { //这里也是 Reply from 10.11.39.2: Destination host unreachable.
                    //System.out.println(ins + " 连接失败");
//                    Log.e(TAG + "failed connected to", ins);
                    return false;
                }
            }
        } catch (IOException e) {
//            Log.e(TAG + " error", String.valueOf(e));
            e.printStackTrace();
        }
        return false;
    }
}
