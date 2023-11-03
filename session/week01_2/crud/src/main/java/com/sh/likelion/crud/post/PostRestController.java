package com.sh.likelion.crud.post;

import com.sh.likelion.crud.exception.PostNotExistException;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import org.slf4j.Logger;

@RestController
@RequestMapping("post")
public class PostRestController {
    private static final Logger logger = LoggerFactory.getLogger(PostRestController.class);
    private final PostService postService;

    public PostRestController(@Autowired PostService postService){
        this.postService = postService;
    }

    // 1 createPost
    // http://localhost:8080/post
    // Post /post
    @PostMapping()
    @ResponseStatus(HttpStatus.CREATED)
    public void createPost(@RequestBody PostDto postDto){
        logger.info(postDto.toString());
        this.postService.createPost(postDto);
    }

    // 2 readPostAll
    // http://localhost:8080/post
    // GET /post
    @GetMapping()
    public List<PostDto> readPostAll(){
        logger.info("in read post all");
        return this.postService.readPostAll();
    }

    // 3 readPost
    // http://localhost:8080/post/1
    // GET /post/1
    @GetMapping("{id}")
    public PostDto readPost(@PathVariable("id") int id){
        logger.info("in read post");
        return this.postService.readPost(id);
    }

    @GetMapping("/test-exception")
    public void throwException() {
        System.out.println("test-exception");
        throw new PostNotExistException();
    }

//    @PutMapping("{id}")
//    public void updatePost(
//            @PathVariable("id") int id,
//            @RequestBody PostDto postDto
//    ){
//        PostDto targetPost = this.postList.get(id);
//        if(postDto.getTitle() != null){
//            targetPost.setTitle(postDto.getTitle());
//        }
//        if(postDto.getContent() != null){
//            targetPost.setContent(postDto.getContent());
//        }
//        if(postDto.getWriter() != null){
//            targetPost.setWriter(postDto.getWriter());
//        }
//        this.postList.set(id, targetPost);
//    }
//
//    @DeleteMapping("{id}")
//    public void deletePost(@PathVariable("id") int id){
//        this.postList.remove(id);
//    }
//
}