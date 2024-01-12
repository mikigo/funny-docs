import {defineConfig} from 'vitepress'
import AutoSidebar from 'vite-plugin-vitepress-auto-sidebar';

// https://vitepress.dev/reference/site-config
export default defineConfig({
    vite: {
        plugins: [
            // add plugin
            AutoSidebar({
                // You can also set options to adjust sidebar data
                // see option document below
                prefix: '.', collapsed: true
            })
        ]
    },
    lang: 'zh-CN',
    title: "Funny Docs",
    description: "有趣的知识库",
    themeConfig: {
        // https://vitepress.dev/reference/default-theme-config

        nav: [
            // { text: '首页', link: '/' },
            {text: '自动化技术', link: '/自动化技术/自动化测试框架/Pytest从入门到起飞'},
            {text: '网络爬虫', link: '/网络爬虫/接口请求工具/Requests'},
            {text: '前后端', link: '/前后端/前端/Linux上安装Node.js'},
            {text: '人工智能', link: '/人工智能/图像/MMDetection入门基础'},
            {text: '编程语言', link: '/编程语言/Python/Python基础语法—8小时入门版'},
            {text: 'Linux', link: '/Linux/方案教程/Linux基础'},
            {text: '技术文档', link: '/技术文档/专利交底书/一种定位目标图片坐标的图像识别技术交底书'},
            {text: '规范文档', link: '/规范文档/流程规范/测试单驱动自动化'},
            {text: '读书笔记', link: '/读书笔记/OpenStack系统架构设计实战'},
            {text: '常见问题', link: '/常见问题/node-error-01'},
            {text: '留言', link: '/comments'},
        ],
        search: {
            provider: 'local'
        },

        // =========================================================
        logo: {src: '/vitepress-logo-mini.svg', width: 24, height: 24},
        socialLinks: [
            {icon: 'github', link: 'https://github.com/mikigo/funny-docs'}
        ],
        footer: {
            copyright: `版权所有 © 2019-${new Date().getFullYear()} 统信软件`
        },

        docFooter: {
            prev: '上一页',
            next: '下一页'
        },

        outline: {
            label: '页面导航'
        },

        lastUpdated: {
            text: '最后更新于',
            formatOptions: {
                dateStyle: 'short',
                timeStyle: 'medium'
            }
        },

        langMenuLabel: '多语言',
        returnToTopLabel: '回到顶部',
        sidebarMenuLabel: '菜单',
        darkModeSwitchLabel: '主题',
        lightModeSwitchTitle: '切换到浅色模式',
        darkModeSwitchTitle: '切换到深色模式'
    },


})