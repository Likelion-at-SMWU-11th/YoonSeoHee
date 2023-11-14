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
                                .authenticated() // 아래가 없다면 anyRequest()에 걸려서 여기를 거침
                                )
                                .formLogin(login -> login
                                        .loginPage("/user/login")
                                        .defaultSuccessUrl("/home") // 로그인 성공 시 돌아가는 페이지 (default로 설정)
                                        .permitAll() // authorize 요청 무시
                                )
                                .logout(logout -> logout
                                        .logoutUrl("/user/logout")
                                        .logoutSuccessUrl("/home") // 로그아웃 성공시 돌아가는 페이지
                                        .deleteCookies("JSESSIONID") // 쿠키 삭제
                                        .invalidateHttpSession(true) // http 세션 객체에 저장해두었던 내용 삭제
                                        .permitAll()
                                );
                                // permitAll: Specify that URLs are allowed by anyone.
                                // authenticated: Specify that URLs are allowed by any authenticated user.
                                // anonymous: Specify that URLs are allowed by anonymous users.


        return http.build();
    }
}
