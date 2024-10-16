CREATE TABLE User_Emotions AS
WITH EmotionCounts AS (
    SELECT 
        user_id, 
        primary_emotion, 
        COUNT(*) AS emotion_count
    FROM 
        emotional_data  -- Replace this with your actual table name if different
    GROUP BY 
        user_id, 
        primary_emotion
),

MaxEmotionCounts AS (
    SELECT 
        user_id, 
        MAX(emotion_count) AS max_count
    FROM 
        EmotionCounts
    GROUP BY 
        user_id
)

SELECT 
    ec.user_id, 
    ec.primary_emotion
FROM 
    EmotionCounts ec
JOIN 
    MaxEmotionCounts mec ON ec.user_id = mec.user_id AND ec.emotion_count = mec.max_count;