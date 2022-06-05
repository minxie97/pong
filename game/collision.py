import constants as c

def handle_collision(ball, left_paddle, right_paddle):
    #ceiling and floor collision
    if ball.y + ball.radius >= c.HEIGHT:
        ball.y_velo *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_velo *= -1

    #paddle collision
    if ball.x_velo < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_velo *= -1

                middle_y = left_paddle.y + left_paddle.height//2
                diff_y = middle_y - ball.y
                reduction_factor = (left_paddle.height//2) / ball.VELO
                
                ball.y_velo = (diff_y / reduction_factor) * -1
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_velo *= -1

                middle_y = right_paddle.y + right_paddle.height//2
                diff_y = middle_y - ball.y
                reduction_factor = (right_paddle.height//2) / ball.VELO
                
                ball.y_velo = (diff_y / reduction_factor) * -1