
provider "aws" {
  access_key = "${var.access_key}"
  secret_key = "${var.secret_key}"
  region = "${var.load_balancer.network.region}"
}

resource "aws_lb_target_group" "main" {
  port = "${var.target_port}"
  protocol = "${upper(var.target_protocol)}"

  health_check {
    enabled = "${var.health_check_path ? true : false}"
    interval = "${var.health_check_interval}"
    path = "${var.health_check_path}"
    matcher = "${join(",", var.healthy_status)}"
    timeout = "${var.health_check_timeout}"
    healthy_threshold = "${var.healthy_threshold}"
    unhealthy_threshold = "${var.unhealthy_threshold}"
  }
}

resource "aws_lb_listener" "main" {
  load_balancer_arn = "${var.load_balancer.lb_arn}"
  port = "${var.port}"
  protocol = "HTTPS"
  ssl_policy = "${var.ssl_policy}"
  certificate_arn = "${var.certificate.cert_arn}"

  default_action {
    type = "forward"
    target_group_arn = "${aws_lb_target_group.main.arn}"
  }

  tags = {
    Name = "cenv-load-balancer"
  }
}
output "listener_id" {
  value = "${aws_lb_listener.main.id}"
}
output "listener_arn" {
  value = "${aws_lb_listener.main.arn}"
}
