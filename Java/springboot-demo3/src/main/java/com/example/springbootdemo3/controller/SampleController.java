package com.example.springbootdemo3.controller;
import com.example.springbootdemo3.domain.Users;
import com.example.springbootdemo3.service.UserService;
import com.github.pagehelper.PageHelper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/user")
public class SampleController {

    final static Logger logger = LoggerFactory.getLogger(SampleController.class);

    @Autowired
    private UserService userService;

//    @Autowired
//    private UserDao userDao;


    @RequestMapping("/info/{userName}")
    public Users getUserInfo(@PathVariable("userName") String userName) {
        return (userService.getUserInfo(userName));
    }


    @RequestMapping("/info")
    public List<Users> getAllUserInfo() {
        return (userService.getAllUserInfo());
    }


    @RequestMapping("/info/p")
    public List<Users> getUserWithPapgerHelper() {
        // 意思是分两页查询，每页两条信息，这是第二页信息，前一个参数是第几页，后一个是页面大小
        PageHelper.startPage(2, 2);
        return (userService.getAllUserInfo());
    }

    @RequestMapping("/add")
    public Users addUser(@RequestParam("userName") String userName, @RequestParam("password") String password, @RequestParam("enabled") int enabled) {
        Users u = new Users();
        u.setEnabled(enabled);
        u.setPassword(password);
        u.setUserName(userName);
        userService.addUser(userName, password, enabled);
        System.out.println(u.toString());
        return u;
    }

    @RequestMapping("/insert")
    public Users insert(@RequestParam("userName") String userName, @RequestParam("password") String password, @RequestParam("enabled") int enabled) {
        Users u1 = new Users();
        u1.setEnabled(enabled);
        u1.setPassword(password);
        u1.setUserName(userName);
        userService.insert(userName, password, enabled);
        return u1;
    }

}
