import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
import launch_ros.actions
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os
import yaml

def generate_launch_description():
    
    return LaunchDescription([
        DeclareLaunchArgument(
            'plan_file',
            default_value='/home/evan/yolodc_ws/src/tensorrt_yolo_ros2/tensorrt_yolo_core/onnx_model/yolov8ndc.plan',
            description='Path to the .plan file'
        ),
        DeclareLaunchArgument(
            'onnx_file',
            default_value='/home/evan/yolodc_ws/src/tensorrt_yolo_ros2/tensorrt_yolo_core/onnx_model/yolov8ndc.onnx',
            description='Path to the .onnx file'
        ),
        DeclareLaunchArgument(
            'nms_thresh',
            default_value='0.7',
            description='Non-Maximum Suppression threshold'
        ),
        DeclareLaunchArgument(
            'conf_thresh',
            default_value='0.7',
            description='Confidence threshold'
        ),
        DeclareLaunchArgument(
            'num_class',
            default_value='1',
            description='Number of classes for object detection'
        ),
        DeclareLaunchArgument(
            'num_kpt',
            default_value='17',
            description='Number of keypoints for pose detection'
        ),
        DeclareLaunchArgument(
            'kpt_dims',
            default_value='3',
            description='Dimensions of keypoints for pose detection'
        ),
        DeclareLaunchArgument(
            'track',
            default_value='true',
            description='Whether to enable tracking'
        ),
        DeclareLaunchArgument(
            'depth',
            default_value='true',
            description='Whether to enable depth camera'
        ),
        DeclareLaunchArgument(
            'pose',
            default_value='false',
            description='Whether to enable pose detection'
        ),
        DeclareLaunchArgument(
            'rgb_image_topic',
            default_value='/camera/camera/color/image_raw',
            description='RGB image topic'
        ),
        DeclareLaunchArgument(
            'depth_image_topic',
            default_value='/camera/camera/depth/image_rect_raw',
            description='Depth image topic'
        ),
        
        # Define the node
        Node(
            package='tensorrt_yolo_ros2',
            executable='camera_infer_node',
            name='yolo_node',
            output='screen',
            parameters=[{
                'track': LaunchConfiguration('track'),
                'depth': LaunchConfiguration('depth'),
                'pose': LaunchConfiguration('pose'),
                'rgbImageTopic': LaunchConfiguration('rgb_image_topic'),
                'depthImageTopic': LaunchConfiguration('depth_image_topic'),
                'planFile': LaunchConfiguration('plan_file'),
                'onnxFile': LaunchConfiguration('onnx_file'),
                'nmsThresh': LaunchConfiguration('nms_thresh'),
                'confThresh': LaunchConfiguration('conf_thresh'),
                'numClass': LaunchConfiguration('num_class'),
                'numKpt': LaunchConfiguration('num_kpt'),
                'kptDims': LaunchConfiguration('kpt_dims')
            }]
        ),
    ])