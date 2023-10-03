package com.sh.likelion.crud;

import com.google.gson.Gson;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class DemoConfig {
    @Bean
    public Gson gson(){
        return new Gson();
    }
}
