# OpenStack系统架构设计实战

## 概述

OpenStack 是一个开源的云计算管理平台项目，在开源云平台中主题讨论数量最大、社区人数最多、提交代码人数最多的平台。支持几乎所有类型的云环境，项目目标是提供实施简单、可大规模扩展、丰富、标准统一的云计算管理平台。

OpenStack 有几个核心组件组成：

计算（Compute）、对象存储（Object Storage）、镜像服务（Image Service）、网络管理（Network）等；

Github：https://github.com/openstack

OpenStack 的用户界面提供了 Web 界面和 Shell 界面，可以通过界面功能进行创建、维护虚拟机等，操作流程有点像 KVM 管理虚拟机的流程；

## 计算（Compute）Nova

Nova 是一套控制器，用于为单个用户或使用群组启动虚拟机实力。OpenStack中实例的整个生命周期中的所有行为都有 Nova 处理，Nova 管理计算资源的创建、销毁、挂起、迁移等功能。

但是，Nova自身并不提供任何虚拟化能力，而是使用支持虚拟化（Hypervisor）的 API 来提供。

Nova 可以多节点部署，支持主流的 Hypervisor 架构，比如：KVM、LXC、QEMU、Xen、Docker等；也能和 VMware 对接；

### nova-api

是用 Python 实现的 Web 服务器，实现 RESTful API 到内部请求消息的转换，实际使用 WSGI 来实现；

### 消息队列（AMQP）

是一个提供统一消息服务的应用层标准高级消息队列协议，基于此协议的客户端和消息中间件可以喘息消息；主要有 2 个组件：Exchange 和 Queue；

### nova-compute

负责管理虚拟机，单独运行于承载分配虚拟机的主机智商，通过消息队列获取任务然后执行。走的是 qemu 那套虚拟化方案；

## 存储管理（Cinder）

Cinder 是在虚拟机和具体的存储设备之间引入一个抽象的 “逻辑存储卷”，整合后端存储设备，并通过统一的 API 接口为云平台提供持久性的块设备存储服务。

### Cinder API

接受客户端发来的HTTP请求，然后进行用户身份认证和消息分发，本质上是一个 WSGI 服务；

### cinder-scheduler

Cinder
