package com.example.auth.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.Customizer;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;

import static org.springframework.security.config.Customizer.withDefaults;

@Configuration
@EnableWebSecurity // spring security를 조작할 준비가 되었음을 스프링 IOC에 알림
public class WebSecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
                .authorizeHttpRequests((authz) -> authz
                                .requestMatchers("/home/**") // home 페이지에 들어가는 URL에 대한 접근 권한 설정
                                .anonymous()
                                .anyRequest()
                                .authenticated()
                                // permitAll: Specify that URLs are allowed by anyone.
                                // authenticated: Specify that URLs are allowed by any authenticated user.
                                // anonymous: Specify that URLs are allowed by anonymous users.
                )
                .formLogin(withDefaults());

        return http.build();
    }
}
