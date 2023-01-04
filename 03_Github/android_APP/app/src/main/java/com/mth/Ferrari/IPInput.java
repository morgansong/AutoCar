package com.mth.Ferrari;


import android.app.Activity;
import android.graphics.Color;
import android.os.Bundle;
import android.os.StrictMode;
import android.util.Log;
import android.widget.TextView;


import com.kongqw.rockerlibrary.view.RockerView;

import cz.msebera.android.httpclient.HttpEntity;
import cz.msebera.android.httpclient.client.config.RequestConfig;
import cz.msebera.android.httpclient.client.methods.CloseableHttpResponse;
import cz.msebera.android.httpclient.client.methods.HttpPost;
import cz.msebera.android.httpclient.entity.StringEntity;
import cz.msebera.android.httpclient.impl.client.CloseableHttpClient;
import cz.msebera.android.httpclient.impl.client.HttpClients;
import cz.msebera.android.httpclient.util.EntityUtils;

import org.json.JSONObject;

public class IPInput extends Activity {

    private TextView mStatus;
    private TextView Switch, go, speedup, left, back, right;


    private boolean flag_runable = false;;
    private TextView mLogRight;

    private boolean flag_start = false;
    private boolean flag_go = false;
    private boolean flag_speedup = false;
    private boolean flag_left = false;
    private boolean flag_back = false;
    private boolean flag_right = false;
    private int acc = 0;

    private String str="";

    private String sw_verion = "2.4";
    //version 2.3 feature:
    //      . sending binaries instead of boolean
    //      . one thread to send the status per 100ms
    //      . disconnection condition is from 5times failed sending
    //          . sending all flags:false if disconnected
    //      . set all timeouts to 100ms
    //      . auto pilot mode

    private int status_marker = 0 ;

    private JSONObject myjson = new JSONObject();

    private String TAG = "MTH_Morgan";


    //    private String myUrl="http://10.11.8.16:5000/myCar";
//    private String myUrl="http://192.168.0.100:5000/myCar";
    private String myUrl;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ip);

        mStatus = (TextView) findViewById(R.id.mystatus);
        mLogRight = (TextView) findViewById(R.id.log_right);

        //android.os.NetworkOnMainThreadException-->W/System.err: android.os.NetworkOnMainThreadException
        if (android.os.Build.VERSION.SDK_INT > 9) {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }

        String IP = getIntent().getStringExtra("ip_address");
        myUrl = "http://" + IP +":5000/myFerrari";
        Log.e(TAG+"myipaddress", myUrl);

        new Thread(readThread).start();

        RockerView rockerViewRight = (RockerView) findViewById(R.id.rockerView_right);
        if (rockerViewRight != null) {
            rockerViewRight.setOnAngleChangeListener(new RockerView.OnAngleChangeListener() {
                @Override
                public void onStart() {
                    flag_go = false;
                    flag_speedup = false;
                    flag_right = false;
                    flag_back = false;
                    flag_left = false;
                    mLogRight.setText(null);
                }

                @Override
                public void angle(double angle, double currentX, double currentY, double centerX, double centerY) throws InterruptedException {
                    // currentX, left-right: 82-740
                    // centerX, middle: 412
                    // currentY, top-bottom: 82-740
                    // centerY, middle: 412
                    mLogRight.setText("摇动角度 : " + angle);
                    Log.e(TAG+"1",  String.valueOf(angle));
                    Log.e(TAG+"2222222",  String.valueOf(currentX));
                    Log.e(TAG+"3333333",  String.valueOf(currentY));

                    if ((int) angle<80 || (int) angle>=280){
                        flag_go = true;
                        flag_right = true;
                        flag_back = false;
                        flag_left = false;
                        acc=0;
                    }

                    if (80<=(int) angle && (int) angle <100){
                        flag_go = false;
                        flag_right = false;
                        flag_back = true;
                        flag_left = false;
                    }

                    if (100<=(int) angle && (int) angle <260){
                        flag_go = true;
                        flag_right = false;
                        flag_back = false;
                        flag_left = true;
                    }

                    if (260<=(int) angle && (int) angle <280){
                        flag_go = true;
                        flag_right = false;
                        flag_back = false;
                        flag_left = false;
                    }

                    acc = PWM_TenTimes(currentX, centerX, currentY, centerY);

                }

                @Override
                public void onFinish() {
                    flag_go = false;
                    flag_speedup = false;
                    flag_right = false;
                    flag_back = false;
                    flag_left = false;
                    acc=0;
                    mLogRight.setText(null);
                }
            });
        }
    }

    int PWM_TenTimes(double currentX, double centerX, double currentY, double centerY){
        return (int) Math.sqrt(Math.pow((currentX-centerX),2)+Math.pow((currentY-centerY),2))*10/330;
    }



    //thread
    Runnable readThread = new Runnable() {
        @Override
        public void run() {
            while (true) {
                try {

                    str = "";
                    if (flag_start) str = str + '1';
                    else str = str + '0';

                    if (flag_go) str = str + '1';
                    else str = str + '0';

                    if (flag_speedup) str = str + '1';
                    else str = str + '0';

                    if (flag_left) str = str + '1';
                    else str = str + '0';

                    if (flag_back) str = str + '1';
                    else str = str + '0';

                    if (flag_right) str = str + '1';
                    else str = str + '0';

                    str = str + String.valueOf(acc);

                    myjson.put("data", str);

                    Log.e(TAG + "---ready", String.valueOf(myjson));
                    String SendResponse = DocHessianServiceTest.sendHttpPost(myUrl, myjson.toString());
                    Log.e(TAG + "---send", String.valueOf(myjson));
                    Log.e(TAG + "---receive", String.valueOf(SendResponse));

                    if (SendResponse.equals("ACK")) {
                        Log.e(TAG + "---changelabel", "changing online");
                        mStatus.setText("Device On-line v"+sw_verion);
                        mStatus.setBackgroundColor(Color.GREEN);
                    }

                    status_marker = 0;


                    Thread.sleep(100);

                } catch (Exception e) {
                    Log.e(TAG + "Exception error", String.valueOf(e));
                    status_marker ++;
                    if(status_marker>5){
                        if (String.valueOf(e).contains("failed to connect to") | String.valueOf(e).contains("timed out")) {
                            Log.e(TAG + "---changelabel", "changing offline");
                            mStatus.setText("Device Off-line v"+sw_verion);
                            mStatus.setBackgroundColor(Color.YELLOW);
                        }
                        status_marker = 0;

                        //avoid sending the previous status while server is off line then on line --> device will immediate reaction --> not good
                        flag_start = false;
                        flag_go = false;
                        flag_speedup = false;
                        flag_right = false;
                        flag_back = false;
                        flag_left = false;
                    }
                    e.printStackTrace();
                }
            }
        }
    };


    //for websocket post
    public static class DocHessianServiceTest {
        public static String sendHttpPost(String url, String regJson) throws Exception {
            CloseableHttpClient httpClient = HttpClients.createDefault();
            RequestConfig requestConfig = RequestConfig.custom().setConnectionRequestTimeout(1000)
                    .setSocketTimeout(1000).setConnectTimeout(1000).build(); //set the timeout

            HttpPost httpPost = new HttpPost(url);
            httpPost.setConfig(requestConfig);
//            httpPost.setProtocolVersion(HttpVersion.HTTP_1_0);
            Log.e("MTH_Morgan 111",  String.valueOf(httpPost));
            httpPost.addHeader("Content-Type", "application/json");
            httpPost.setEntity(new StringEntity(regJson,"UTF-8")); //防止中文乱码

            CloseableHttpResponse response = httpClient.execute(httpPost);
            System.out.println(response.getStatusLine().getStatusCode() + "\n");
            Log.e("MTH_Morgan222",  String.valueOf(response));
            HttpEntity entity = response.getEntity();
            Log.e("MTH_Morgan333",  String.valueOf(entity));
            Log.e("MTH_Morgan333",  String.valueOf(response.getStatusLine()));
//            String responseContent = EntityUtils.toString(entity, "UTF-8");   //Premature end of Content-Length delimited message body
            Log.e("MTH_Morgan444",  String.valueOf(response.getStatusLine().getStatusCode()));
//            Log.e("MTH_Morgan555",  String.valueOf(responseContent));

            String responseString = EntityUtils.toString(response.getEntity());
            Log.e("MTH_Morgan666",  String.valueOf(responseString));

            response.close();
            httpClient.close();
//            return responseContent;
            return responseString;
        }

    }
}
