require 'csv'
require 'colorize'

module CaliforniaRealEstateExamPrep

  class PracticeExam

    QUESTIONS_DATABASE = 'database.csv'
    COLUMN_HEADERS = ['subject', 'question', 'answer_a', 'answer_b', 'answer_c', 'answer_d', 'hint']

    def initialize
      @progress = { correct: 0, incorrect: 0 }

      rows = CSV.read(QUESTIONS_DATABASE, { headers: :first_row })
      row_count = rows.count
      while true
        random_row_index = Random.new.rand(0...row_count)
        random_row = rows[random_row_index]
        print_question_from_row(random_row)
        answer = gets.chomp
        check_answer(random_row, answer)
        print_exam_progress
      end
    end

    private

    def check_answer(row, answer)
      if answer == row['answer']
        @progress[:correct] += 1
        print_correct_answer
      else
        @progress[:incorrect] += 1
        answer_hint = row['hint']
        print_incorrect_answer(answer_hint)
      end
    end

    def print_correct_answer
      print "#{"That is the correct answer.".light_green}\n\n"
    end

    def print_incorrect_answer(hint)
      print "#{hint.light_red}\n\n"
    end

    def print_exam_progress
      term_width = `tput cols`.to_i
      score = "Score: #{percent_correct}%"
      progress = "(#{@progress[:correct]} correct / #{questions_answered} answered)"

      print "#{score.ljust(term_width - progress.length)}#{progress}".white.on_light_black
      puts
    end

    def questions_answered
      @progress[:correct] + @progress[:incorrect]
    end

    def percent_correct
      ((@progress[:correct].to_f / questions_answered.to_f) * 100).round(2)
    end

    def print_question_from_row(row)
      puts
      print "[#{row['subject']}]\n".yellow
      print "#{row['question']}\n\n"
      print " a) #{row['answer_a']}\n"
      print " b) #{row['answer_b']}\n"
      print " c) #{row['answer_c']}\n"
      print " d) #{row['answer_d']}\n\n"
      print "Your Answer: "
    end
  end
end

CaliforniaRealEstateExamPrep::PracticeExam.new
