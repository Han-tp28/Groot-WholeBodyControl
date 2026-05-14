/**
 * @file policy_parameters.hpp
 * @brief Motor constants, PID gains, joint mappings, action scales, and default
 *        standing angles for the selected deploy robot policy.
 *
 * ## Joint Ordering
 *
 * Two ordering conventions coexist in the codebase:
 *  - **MuJoCo order** – used by the simulator, reference motions, and output
 *    interfaces.  Joint indices follow the URDF kinematic tree.
 *  - **IsaacLab order** – used internally by the RL policy and the robot SDK.
 *    Interleaves left/right joints differently.
 *
 * The arrays `isaaclab_to_mujoco` and `mujoco_to_isaaclab` provide the
 * remapping between the two orderings.
 *
 * ## PID Gain Computation
 *
 * Stiffness (Kp) and damping (Kd) values are computed from motor armature
 * constants using a second-order critically-damped model:
 *   - stiffness = armature × ω²   (ω = 10 Hz × 2π)
 *   - damping   = 2 × ζ × armature × ω   (ζ = 2.0)
 *
 * ## Action Scaling
 *
 * Policy actions are scaled by:
 *   action_scale = 0.25 × effort_limit / stiffness
 *
 * The final joint target is: target = action × action_scale + default_angle.
 */

#ifndef POLICY_PARAMETERS_HPP
#define POLICY_PARAMETERS_HPP

#include <array>
#include <vector>

#include "robot_parameters.hpp"

const double ONE_DEGREE = 0.0174533;  ///< One degree in radians.

// Motor armature constants (used for PID gain computation)
const double ARMATURE_5020 = 0.003609725;
const double ARMATURE_7520_14 = 0.010177520;
const double ARMATURE_7520_22 = 0.025101925;
const double ARMATURE_4010 = 0.00425;

// Control parameters for PID gain computation
const double NATURAL_FREQ = 10 * 2.0 * 3.1415926535; // 10Hz
const double DAMPING_RATIO = 2;

// Computed stiffness values: stiffness = armature * natural_freq^2
const double STIFFNESS_5020 = ARMATURE_5020 * NATURAL_FREQ * NATURAL_FREQ;
const double STIFFNESS_7520_14 = ARMATURE_7520_14 * NATURAL_FREQ * NATURAL_FREQ;
const double STIFFNESS_7520_22 = ARMATURE_7520_22 * NATURAL_FREQ * NATURAL_FREQ;
const double STIFFNESS_4010 = ARMATURE_4010 * NATURAL_FREQ * NATURAL_FREQ;

// Computed damping values: damping = 2.0 * damping_ratio * armature * natural_freq
const double DAMPING_5020 = 2.0 * DAMPING_RATIO * ARMATURE_5020 * NATURAL_FREQ;
const double DAMPING_7520_14 = 2.0 * DAMPING_RATIO * ARMATURE_7520_14 * NATURAL_FREQ;
const double DAMPING_7520_22 = 2.0 * DAMPING_RATIO * ARMATURE_7520_22 * NATURAL_FREQ;
const double DAMPING_4010 = 2.0 * DAMPING_RATIO * ARMATURE_4010 * NATURAL_FREQ;

// Effort limits for different motor types (used for action scale computation)
const double EFFORT_LIMIT_5020 = 25.0;    // 5020 motor type
const double EFFORT_LIMIT_7520_14 = 88.0; // 7520_14 motor type
const double EFFORT_LIMIT_7520_22 = 139.0; // 7520_22 motor type
const double EFFORT_LIMIT_4010 = 5.0;     // 4010 motor type


// VR5Point index (isaaclab index) left wrist, right wrist, pelvs, left ankle, right ankle
const std::array<int, 5> vr_5point_index = {28, 29, 0, 18, 19};

// Joint mapping arrays
// VR3Point index (isaaclab index) left wrist, right wrist, torso,
const std::array<int, 3> vr_3point_index = {28, 29, 9};

// Upper body joint index (mujoco order)
const std::vector<int> upper_body_joint_mujoco_order_in_isaaclab_index = { 2, 5, 8, 11, 15, 19, 21, 23, 25, 27, 12, 16, 20, 22, 24, 26, 28};
const std::vector<int> upper_body_joint_mujoco_order_in_mujoco_index = { 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28};

// upper body joint index (isaaclab order)
const std::vector<int> upper_body_joint_isaaclab_order_in_isaaclab_index = { 2, 5, 8, 11, 12, 15, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28};
const std::vector<int> upper_body_joint_isaaclab_order_in_mujoco_index = { 12, 13, 14, 15, 22, 16, 23, 17, 24, 18, 25, 19, 26, 20, 27, 21, 28};

// wrist joint index (mujoco order)
const std::vector<int> wrist_joint_mujoco_order_in_isaaclab_index = {23, 25, 27, 24, 26, 28};
const std::vector<int> wrist_joint_mujoco_order_in_mujoco_index = {19, 20, 21, 26, 27, 28};

// wrist joint index (isaaclab order)
#if defined(DEPLOY_ROBOT_VR_H3_1)
const std::vector<int> wrist_joint_isaaclab_order_in_isaaclab_index = {18, 19, 20, 25, 26, 27};
const std::vector<int> wrist_joint_isaaclab_order_in_mujoco_index = {22, 23, 24, 25, 26, 27};
#else
const std::vector<int> wrist_joint_isaaclab_order_in_isaaclab_index = {23, 24, 25, 26, 27, 28};
const std::vector<int> wrist_joint_isaaclab_order_in_mujoco_index = {19, 26, 20, 27, 21, 28};
#endif

// lower body joint index (mujoco order)
const std::vector<int> lower_body_joint_mujoco_order_in_isaaclab_index = {0, 3, 6, 9, 13, 17, 1, 4, 7, 10, 14, 18};
const std::vector<int> lower_body_joint_mujoco_order_in_mujoco_index = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11};

// lower body joint index (isaaclab order)
const std::vector<int> lower_body_joint_isaaclab_order_in_isaaclab_index = {0, 1, 3, 4, 6, 7, 9, 10, 13, 14, 17, 18};
const std::vector<int> lower_body_joint_isaaclab_order_in_mujoco_index = {0, 6, 1, 7, 2, 8, 3, 9, 4, 10, 5, 11};

// Joint mapping arrays for the selected deploy robot.
#if defined(DEPLOY_ROBOT_VR_H3_1)
const std::array<int, G1_NUM_MOTOR> isaaclab_to_mujoco = {
    0, 3, 6, 10, 14, 18, 1, 4, 7, 11, 15, 19, 2, 5,
    8, 12, 16, 20, 22, 24, 26, 9, 13, 17, 21, 23, 25, 27
};
const std::array<int, G1_NUM_MOTOR> mujoco_to_isaaclab = {
    0, 6, 12, 1, 7, 13, 2, 8, 14, 21, 3, 9, 15, 22,
    4, 10, 16, 23, 5, 11, 17, 24, 18, 25, 19, 26, 20, 27
};
#else
const std::array<int, G1_NUM_MOTOR> isaaclab_to_mujoco = {
    0, 3, 6, 9, 13, 17, 1, 4, 7, 10, 14, 18, 2, 5, 8,
    11, 15, 19, 21, 23, 25, 27, 12, 16, 20, 22, 24, 26, 28
};
const std::array<int, G1_NUM_MOTOR> mujoco_to_isaaclab = {
    0, 6, 12, 1, 7, 13, 2, 8, 14, 3, 9, 15, 22, 4, 10,
    16, 23, 5, 11, 17, 24, 18, 25, 19, 26, 20, 27, 21, 28
};
#endif

// Action scaling parameters
// Computed using: action_scale = 0.25 * effort_limit / stiffness
// Based on actuator configurations from IsaacLab G1_CYLINDER_CFG
#if defined(DEPLOY_ROBOT_VR_H3_1)
const std::array<double, G1_NUM_MOTOR> g1_action_scale = {
    0.25 * 369.0 / 913.0, 0.25 * 369.0 / 906.0, 0.25 * 191.0 / 155.0,
    0.25 * 369.0 / 561.0, 0.25 * 140.0 / 658.0, 0.25 * 140.0 / 646.0,
    0.25 * 369.0 / 913.0, 0.25 * 369.0 / 906.0, 0.25 * 191.0 / 155.0,
    0.25 * 369.0 / 561.0, 0.25 * 140.0 / 658.0, 0.25 * 140.0 / 646.0,
    0.25 * 102.0 / 367.0, 0.25 * 102.0 / 367.0,
    0.25 * 66.0 / 103.0, 0.25 * 66.0 / 94.0, 0.25 * 66.0 / 291.0,
    0.25 * 66.0 / 291.0, 0.25 * 34.0 / 291.0, 0.25 * 11.0 / 213.0,
    0.25 * 11.0 / 212.0,
    0.25 * 66.0 / 103.0, 0.25 * 66.0 / 94.0, 0.25 * 66.0 / 291.0,
    0.25 * 66.0 / 291.0, 0.25 * 34.0 / 291.0, 0.25 * 11.0 / 213.0,
    0.25 * 11.0 / 212.0,
};
#else
const std::array<double, G1_NUM_MOTOR> g1_action_scale = {
    0.25 * EFFORT_LIMIT_7520_22 / STIFFNESS_7520_22,
    0.25 * EFFORT_LIMIT_7520_22 / STIFFNESS_7520_22,
    0.25 * EFFORT_LIMIT_7520_14 / STIFFNESS_7520_14,
    0.25 * EFFORT_LIMIT_7520_22 / STIFFNESS_7520_22,
    0.25 * EFFORT_LIMIT_5020 / STIFFNESS_5020,
    0.25 * EFFORT_LIMIT_5020 / STIFFNESS_5020,
    0.25 * EFFORT_LIMIT_7520_22 / STIFFNESS_7520_22,
    0.25 * EFFORT_LIMIT_7520_22 / STIFFNESS_7520_22,
    0.25 * EFFORT_LIMIT_7520_14 / STIFFNESS_7520_14,
    0.25 * EFFORT_LIMIT_7520_22 / STIFFNESS_7520_22,
    0.25 * EFFORT_LIMIT_5020 / STIFFNESS_5020,
    0.25 * EFFORT_LIMIT_5020 / STIFFNESS_5020,
    0.25 * EFFORT_LIMIT_7520_14 / STIFFNESS_7520_14,
    0.25 * EFFORT_LIMIT_5020 / STIFFNESS_5020,
    0.25 * EFFORT_LIMIT_5020 / STIFFNESS_5020,
    0.25 * EFFORT_LIMIT_5020 / STIFFNESS_5020,
    0.25 * EFFORT_LIMIT_5020 / STIFFNESS_5020,
    0.25 * EFFORT_LIMIT_5020 / STIFFNESS_5020,
    0.25 * EFFORT_LIMIT_5020 / STIFFNESS_5020,
    0.25 * EFFORT_LIMIT_5020 / STIFFNESS_5020,
    0.25 * EFFORT_LIMIT_4010 / STIFFNESS_4010,
    0.25 * EFFORT_LIMIT_4010 / STIFFNESS_4010,
    0.25 * EFFORT_LIMIT_5020 / STIFFNESS_5020,
    0.25 * EFFORT_LIMIT_5020 / STIFFNESS_5020,
    0.25 * EFFORT_LIMIT_5020 / STIFFNESS_5020,
    0.25 * EFFORT_LIMIT_5020 / STIFFNESS_5020,
    0.25 * EFFORT_LIMIT_5020 / STIFFNESS_5020,
    0.25 * EFFORT_LIMIT_4010 / STIFFNESS_4010,
    0.25 * EFFORT_LIMIT_4010 / STIFFNESS_4010,
};
#endif

// PID control gains - Position gains (Kp)
// These values are computed based on the stiffness constants above
#if defined(DEPLOY_ROBOT_VR_H3_1)
const std::array<float, G1_NUM_MOTOR> kps = {
    913.0f, 906.0f, 155.0f, 561.0f, 658.0f, 646.0f,
    913.0f, 906.0f, 155.0f, 561.0f, 658.0f, 646.0f,
    367.0f, 367.0f,
    103.0f, 94.0f, 291.0f, 291.0f, 291.0f, 213.0f, 212.0f,
    103.0f, 94.0f, 291.0f, 291.0f, 291.0f, 213.0f, 212.0f,
};
#else
const std::array<float, G1_NUM_MOTOR> kps = {
    STIFFNESS_7520_22, STIFFNESS_7520_22, STIFFNESS_7520_14,
    STIFFNESS_7520_22, 2.0 * STIFFNESS_5020, 2.0 * STIFFNESS_5020,
    STIFFNESS_7520_22, STIFFNESS_7520_22, STIFFNESS_7520_14,
    STIFFNESS_7520_22, 2.0 * STIFFNESS_5020, 2.0 * STIFFNESS_5020,
    STIFFNESS_7520_14, 2.0 * STIFFNESS_5020, 2.0 * STIFFNESS_5020,
    STIFFNESS_5020, STIFFNESS_5020, STIFFNESS_5020, STIFFNESS_5020,
    STIFFNESS_5020, STIFFNESS_4010, STIFFNESS_4010,
    STIFFNESS_5020, STIFFNESS_5020, STIFFNESS_5020, STIFFNESS_5020,
    STIFFNESS_5020, STIFFNESS_4010, STIFFNESS_4010,
};
#endif

// PID control gains - Derivative gains (Kd)
// These values are computed based on the damping constants above
#if defined(DEPLOY_ROBOT_VR_H3_1)
const std::array<float, G1_NUM_MOTOR> kds = {
    73.0f, 72.0f, 12.0f, 45.0f, 35.0f, 34.0f,
    73.0f, 72.0f, 12.0f, 45.0f, 35.0f, 34.0f,
    29.0f, 29.0f,
    8.0f, 7.0f, 23.0f, 23.0f, 12.0f, 8.0f, 8.0f,
    8.0f, 7.0f, 23.0f, 23.0f, 12.0f, 8.0f, 8.0f,
};
#else
const std::array<float, G1_NUM_MOTOR> kds = {
    DAMPING_7520_22, DAMPING_7520_22, DAMPING_7520_14,
    DAMPING_7520_22, 2.0 * DAMPING_5020, 2.0 * DAMPING_5020,
    DAMPING_7520_22, DAMPING_7520_22, DAMPING_7520_14,
    DAMPING_7520_22, 2.0 * DAMPING_5020, 2.0 * DAMPING_5020,
    DAMPING_7520_14, 2.0 * DAMPING_5020, 2.0 * DAMPING_5020,
    DAMPING_5020, DAMPING_5020, DAMPING_5020, DAMPING_5020,
    DAMPING_5020, DAMPING_4010, DAMPING_4010,
    DAMPING_5020, DAMPING_5020, DAMPING_5020, DAMPING_5020,
    DAMPING_5020, DAMPING_4010, DAMPING_4010,
};
#endif

// Default joint angles (standing pose)
#if defined(DEPLOY_ROBOT_VR_H3_1)
const std::array<double, G1_NUM_MOTOR> default_angles = {
    -0.2, 0.0, 0.0, 0.4, -0.2, 0.0,
    -0.2, 0.0, 0.0, 0.4, -0.2, 0.0,
    0.0, 0.0,
    0.0, 0.2, 0.0, 1.0, 0.0, 0.0, 0.0,
    0.0, -0.2, 0.0, 1.0, 0.0, 0.0, 0.0
};
#else
const std::array<double, G1_NUM_MOTOR> default_angles = {
    -0.312, 0.0, 0.0, 0.669, -0.363, 0.0,
    -0.312, 0.0, 0.0, 0.669, -0.363, 0.0,
    0.0, 0.0, 0.0,
    0.2, 0.2, 0.0, 0.6, 0.0, 0.0, 0.0,
    0.2, -0.2, 0.0, 0.6, 0.0, 0.0, 0.0
};
#endif

#endif // POLICY_PARAMETERS_HPP
