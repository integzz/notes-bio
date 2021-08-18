from jinja2.utils import generate_lorem_ipsum


@app.route('/post')
def show_post():
    post_body = generate_lorem_ipsum(n=2)  #生成两段随机文本
    return f'''
        <hl>A very long post</hl>
        <div class="body">{post_body}</div>
        <button id="load">Load More</button>
        <script src="https://code.jquery.com/jquery-3.3.1.min.js">
        </script＞
            <script type="text/javascript">
            $(function() {
                $("#load").click(function() {
                    $.ajax({
                        url: "/more",
                        type: "get",
                        success: function (data) {
                    $(".body").append(data);
                    }
                });
                });
            });
        </script>
    '''
