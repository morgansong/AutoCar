package com.mth.rpi_cam;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.KeyEvent;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;


public class MainActivity extends AppCompatActivity {

    private WebView webview;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
//        if (getSupportActionBar() != null) {
//            getSupportActionBar().hide();
//        }
        webview = (WebView) findViewById(R.id.webview);


        load();


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
        webview.loadUrl("http://192.168.43.209:8081/");
//        webview.loadUrl("https://www.baidu.com/");
    }
}

