package com.sh.likelion.crud.post;

//import org.slf4j.Logger;
//import org.slf4j.LoggerFactory;
//import org.springframework.stereotype.Controller;
//import org.springframework.web.bind.annotation.*;
//
//import java.util.ArrayList;
//import java.util.List;
//
//@Controller
//@ResponseBody
//@RequestMapping("post")
//public class PostController {
//    private static final Logger logger = LoggerFactory.getLogger(PostController.class);
//    private final List<PostDto> postList;
//
//    public PostController(){
//        postList=new ArrayList<>();
//    }
//
//    @PostMapping("create")
//    public void createPost(@RequestBody PostDto postDto){
//        logger.info(postDto.toString());
//        this.postList.add(postDto);
//    }
//
//    @GetMapping("read-all")
//    public List<PostDto> readPostAll(){
//        logger.info("in read all");
//        return this.postList;
//    }
//
//    @GetMapping("read-one")
//    public PostDto readPostOne(@RequestParam("id") int id){
//        logger.info("in read one");
//        return this.postList.get(id);
//    }
//
//    @PostMapping("update")
//    public void updatePost(
//        @RequestParam("id") int id,
//        @RequestBody PostDto postDto
//    ){
//        PostDto targetPost = this.postList.get(id);
//        if(postDto.getTitle() != null){
//            targetPost.setTitle(postDto.getTitle());
//        }
//        if(postDto.getContent() != null){
//            targetPost.setContent(postDto.getContent());
//        }
//        this.postList.set(id, targetPost);
//    }
//
//    @DeleteMapping("delete")
//    public void deletePost(@RequestParam("id") int id){
//        this.postList.remove(id);
//    }
//}

import com.google.gson.Gson;
import com.sh.likelion.crud.GsonComponent;
import com.sh.likelion.crud.ValidTestDto;
import com.sh.likelion.crud.aspect.LogArguments;
import com.sh.likelion.crud.aspect.LogExecutionTime;
import com.sh.likelion.crud.aspect.LogParameters;
import com.sh.likelion.crud.aspect.LogReturn;
import com.sh.likelion.crud.post.PostDto;
import com.sh.likelion.crud.post.PostService;
import org.slf4j.LoggerFactory;
import org.slf4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@RestController
@RequestMapping("Post")
public class PostController {
    private static final Logger logger = LoggerFactory.getLogger(PostController.class);
    private final PostService postService;

    // private final Gson gson;

    public PostController(
            @Autowired PostService postService
            // @Autowired Gson gson
            // @Autowired GsonComponent gson
    ){
        this.postService=postService;
        // logger.info(gson.toString());
        // this.gson = gson.getGson();
    }

    @LogArguments
    @PostMapping()
    @ResponseStatus(HttpStatus.CREATED)
    public void createPost(@Valid @RequestBody PostDto postDto){
        this.postService.createPost(postDto);
    }

    @LogReturn
    @GetMapping("{id}")
    public PostDto readPost(@PathVariable("id") int id){
        return this.postService.readPost(id);
    }

    @LogExecutionTime

    @GetMapping("")
    public List<PostDto> readPostAll(){
        return this.postService.readPostAll();
    }

    @PutMapping("{id}")
    @ResponseStatus(HttpStatus.ACCEPTED)
    public void updatePost(@PathVariable("id") int id, @RequestBody PostDto postDto){
        this.postService.updatePost(id, postDto);
    }

    @DeleteMapping("{id}")
    @ResponseStatus(HttpStatus.ACCEPTED)
    public void deletePost(@PathVariable("id") int id){
        this.postService.deletePost(id);
    }

    @GetMapping("test-log")
    public void testlog(){
        logger.trace("A TRACE Message");
        logger.trace("A DEBUG Message");
        logger.trace("An INFO Message");
        logger.trace("A WARN Message");
        logger.trace("An ERROR Message");
    }

    @PostMapping("test-valid")
    public void testValue(@Valid @RequestBody ValidTestDto dto) {
        logger.info(dto.toString());
    }
}