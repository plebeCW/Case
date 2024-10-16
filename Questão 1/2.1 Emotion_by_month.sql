CREATE TABLE Emotion_By_Month AS
WITH EmotionCounts AS (
    SELECT 
        user_id, 
        primary_emotion, 
        strftime('%Y-%m', timestamp) AS month_year,
        COUNT(*) AS emotion_count
    FROM 
        emotional_data
    GROUP BY 
        user_id, 
        primary_emotion,
        month_year
),

MaxEmotionCounts AS (
    SELECT 
        user_id, 
        month_year,
        MAX(emotion_count) AS max_count
    FROM 
        EmotionCounts
    GROUP BY 
        user_id,
        month_year
)

SELECT 
    ec.user_id, 
    ec.primary_emotion,
    ec.month_year
FROM 
    EmotionCounts ec
JOIN 
    MaxEmotionCounts mec ON ec.user_id = mec.user_id AND ec.month_year = mec.month_year AND ec.emotion_count = mec.max_count;