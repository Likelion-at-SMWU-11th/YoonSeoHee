package com.sh.likelion.crud.post;

import lombok.Getter;
import lombok.Setter;

import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;

@Getter
@Setter
public class PostDto {
    private int id;
    @NotNull
    private String title;
    @Size(max = 400)
    private String content;
    @Size(min = 3, max = 10)
    private String writer;
//    private int boardId;

    public PostDto(int id, String title, String content, String writer){
        this.id = id;
        this.title = title;
        this.content = content;
        this.writer = writer;
//        this.boardId = boardId;
    }

    public PostDto(){
        this.title = title;
        this.content = content;
        this.writer = writer;
    }
}
