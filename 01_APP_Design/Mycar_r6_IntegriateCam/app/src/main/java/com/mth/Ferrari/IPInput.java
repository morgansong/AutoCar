package com.mth.Ferrari;


import android.app.Activity;
import android.graphics.Color;
import android.os.Bundle;
import android.os.StrictMode;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;


import cz.msebera.android.httpclient.HttpEntity;
import cz.msebera.android.httpclient.HttpVersion;
import cz.msebera.android.httpclient.client.config.RequestConfig;
import cz.msebera.android.httpclient.client.methods.CloseableHttpResponse;
import cz.msebera.android.httpclient.client.methods.HttpPost;
import cz.msebera.android.httpclient.entity.StringEntity;
import cz.msebera.android.httpclient.impl.client.CloseableHttpClient;
import cz.msebera.android.httpclient.impl.client.HttpClients;
import cz.msebera.android.httpclient.util.EntityUtils;

import org.json.JSONException;
import org.json.JSONObject;

public class IPInput extends Activity {

    private TextView mStatus;
    private TextView Switch, go, speedup, left, back, right;
    private Button ACCELERATOR;
    private WebView webview;


    private boolean flag_runable = false;

    private boolean flag_start = false;
    private boolean flag_go = false;
    private boolean flag_speedup = false;
    private boolean flag_left = false;
    private boolean flag_back = false;
    private boolean flag_right = false;

    private String str="";

    private String sw_verion = "2.31";
    //version 2.3 feature:
    //      . sending binaries instead of boolean
    //      . one thread to send the status per 100ms
    //      . disconnection condition is from 5times failed sending
    //          . sending all flags:false if disconnected
    //      . set all timeouts to 100ms
    //      . dynamic acc speed
    //      . integriate the camera

    private int status_marker = 0 ;

    private JSONObject myjson = new JSONObject();

    private String TAG = "MTH_Morgan";

//    private String myUrl="http://10.11.8.16:5000/myCar";
//    private String myUrl="http://192.168.0.100:5000/myCar";
    private String myUrl,camUrl;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ip);

        mStatus = (TextView) findViewById(R.id.mystatus);

        ACCELERATOR = (Button)findViewById(R.id.ACCELERATOR);

        //android.os.NetworkOnMainThreadException-->W/System.err: android.os.NetworkOnMainThreadException
        if (android.os.Build.VERSION.SDK_INT > 9) {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }

        String IP = getIntent().getStringExtra("ip_address");
        myUrl = "http://" + IP +":5000/myFerrari";
        camUrl = "http://" + IP +":8081";
        Log.e(TAG+"myipaddress", myUrl);

        new Thread(readThread).start();

        final Button Switch = findViewById(R.id.Switch);
        Switch.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                flag_runable = true;

                flag_go = false;
                flag_speedup = false;
                flag_right = false;
                flag_back = false;
                flag_left = false;
            }
        });



        final Button go = findViewById(R.id.GO);
        go.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                flag_runable = true;

                flag_go = true;
                flag_speedup = false;
                flag_left = false;
                flag_back = false;
                flag_right = false;
            }
        });



        final Button speedup = findViewById(R.id.ACCELERATOR);
        speedup.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                flag_runable = true;

//                flag_go = false;
                if(flag_speedup) {
                    flag_speedup = false;
                    ACCELERATOR.setText("Hi_Speed");
                }
                else {
                    flag_speedup = true;
                    ACCELERATOR.setText("Lo_Speed");
                }
//                flag_left = false;
//                flag_back = false;
//                flag_right = false;
            }
        });


        final Button left = findViewById(R.id.LEFT);
        left.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                flag_runable = true;

                flag_go = true;
                flag_speedup = false;
                flag_left = true;
                flag_back = false;
                flag_right = false;
            }
        });


        final Button back = findViewById(R.id.BACK);
        back.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                flag_runable = true;

                flag_go = false;
                flag_speedup = false;
                flag_left = false;
                flag_back = true;
                flag_right = false;
            }
        });


        final Button right = findViewById(R.id.RIGHT);
        right.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                flag_runable = true;

                flag_go = true;
                flag_speedup = false;
                flag_left = false;
                flag_back = false;
                flag_right = true;
            }
        });

        webview = (WebView) findViewById(R.id.webview);
        load();
    }

    public void Covert() {
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
    private void load() {
        WebSettings webviewSettings = webview.getSettings();
        webviewSettings.setJavaScriptEnabled(true);
        webviewSettings.setJavaScriptEnabled(true);
        webviewSettings.setJavaScriptCanOpenWindowsAutomatically(true);
        webviewSettings.setAllowFileAccess(true);// 设置允许访问文件数据
        webviewSettings.setSupportZoom(true);
        webviewSettings.setBuiltInZoomControls(true);
        webviewSettings.setJavaScriptCanOpenWindowsAutomatically(true);
        webviewSettings.setCacheMode(WebSettings.LOAD_CACHE_ELSE_NETWORK);
        webviewSettings.setDomStorageEnabled(true);
        webviewSettings.setDatabaseEnabled(true);

        //设置载入页面自适应手机屏幕，居中显示

        webviewSettings.setUseWideViewPort(true);
        webviewSettings.setLoadWithOverviewMode(true);
//        webview.setWebViewClient(new WebViewClient());

        webview.setWebChromeClient(new WebChromeClient());
        webview.loadUrl(camUrl);
//        webview.loadUrl("https://www.baidu.com/");
    }
}
