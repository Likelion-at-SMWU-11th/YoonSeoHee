package com.sh.likelion.crud;


import com.sh.likelion.crud.exception.BaseException;
import com.sh.likelion.crud.exception.ErrorResponseDto;
import com.sh.likelion.crud.exception.PostNotExistException;
import com.sh.likelion.crud.exception.PostNotInBoardException;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.server.ResponseStatusException;

@RestController
@RequestMapping("except")
public class ExceptionTestController {

    @GetMapping("/{id}")
    public void throwException(@PathVariable int id){
        switch (id) {
            case 2:
                throw new PostNotInBoardException();
            case 1:
                throw new PostNotExistException();

            default:
                throw new ResponseStatusException(HttpStatus.NOT_FOUND);
        }
    }

//    @ExceptionHandler(BaseException.class)
//    @ResponseStatus(HttpStatus.BAD_REQUEST)
//    public ErrorResponseDto handleBaseException(BaseException exception) {
//        return new ErrorResponseDto(exception.getMessage());
//    }
}
