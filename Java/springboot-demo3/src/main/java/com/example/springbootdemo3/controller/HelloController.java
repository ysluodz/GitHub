package com.example.springbootdemo3.controller;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController //@RestController 的意思就是controller里面的方法都以json格式输出，不用再写什么jackjson配置的了！
@EnableAutoConfiguration
public class HelloController {

    @RequestMapping(value="/hello",method= RequestMethod.GET)
    public String sayHello(){
        return "hello good!";
    }


    @RequestMapping("/hello/{name}")
    public String word(@PathVariable String name) {
        return "word--spring boot:" + name;
    }
}
