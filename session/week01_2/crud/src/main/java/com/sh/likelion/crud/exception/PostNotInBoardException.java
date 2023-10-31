package com.sh.likelion.crud.exception;

public class PostNotInBoardException extends BaseException {
    public PostNotInBoardException() {
        super("target post is not in board");
    }
}
